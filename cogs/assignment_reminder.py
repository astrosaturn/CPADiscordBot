import disnake
from disnake.ext import commands, tasks
from datetime import datetime, timedelta

from models.db.database import Database
from models.db.models.reminder import Reminder


# Eric Poroznik

class AssignmentReminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_reminders.start()

    @commands.slash_command(description="Set a reminder for an assignment (YYYY-MM-DD HH:MM)")
    async def remind(
        self,
        interaction: disnake.ApplicationCommandInteraction,
        name: str,
        due_date: str = None,  # format: YYYY-MM-DD
        time: str = None       # format: HH:MM
    ):
        # parse the due date, defaulting to today if not provided
        if due_date:
            try:
                due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                await interaction.response.send_message("Invalid date format. Use `YYYY-MM-DD`.")
                return
        else:
            due_date_obj = datetime.now().date()  

        # parse the time, defaulting to the current time if not provided
        if time:
            try:
                due_time_obj = datetime.strptime(time, "%H:%M").time()
            except ValueError:
                await interaction.response.send_message("Invalid time format. Use `HH:MM`.")
                return
        else:
            due_time_obj = datetime.now().time().replace(second=0, microsecond=0)

        due_datetime = datetime.combine(due_date_obj, due_time_obj)
        reminder_time = due_datetime - timedelta(hours=2)

        session = Database.create_session()

        new_reminder = Reminder.insert(
            discordUserId=interaction.author.id,
            channelId=interaction.channel_id,
            name=name,
            dueDatetime=due_datetime,
            reminderTime=reminder_time,
            session=session
        )

        session.close()
        await interaction.response.send_message(f"Reminder set for assignment '{name}' due on {due_datetime}.")

    @tasks.loop(minutes=1)
    async def check_reminders(self):
        now = datetime.now()
        session = Database.create_session()
        for reminder in Reminder.get_all(session):  # iterate over list
            if now >= reminder.getReminderTime():
                user = self.bot.get_user(reminder.discordUserId)
                channel = self.bot.get_channel(reminder.channelId)

                if user and channel:
                    embed = disnake.Embed(
                        title=f"Assignment: {reminder.name}",
                        description=f"Due at: {reminder.dueDatetime}",
                        url="https://blackboard.sl.on.ca/ultra/calendar",
                    )
                    embed.set_author(
                        name=user.display_name,
                        icon_url=user.avatar.url if user.avatar else ""
                    )
                    await channel.send(f"{user.mention}", embed=embed)

                Reminder.delete(reminder.discordUserId, reminder.name, session)
        session.close()

    @check_reminders.before_loop
    async def before_check_reminders(self):
        await self.bot.wait_until_ready()  

def setup(bot):
    bot.add_cog(AssignmentReminder(bot))
