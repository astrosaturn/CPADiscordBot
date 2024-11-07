import disnake
from disnake.ext import commands, tasks
from datetime import datetime, timedelta

class AssignmentReminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminders = []  
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
            due_time_obj = datetime.now().time() 

        due_datetime = datetime.combine(due_date_obj, due_time_obj)
        reminder_time = due_datetime - timedelta(hours=2) 

        self.reminders.append({
            "user": interaction.author.id,
            "channel": interaction.channel_id,
            "name": name,
            "due_datetime": due_datetime,
            "reminder_time": reminder_time
        })

        await interaction.response.send_message(f"Reminder set for assignment '{name}' due on {due_datetime}.")

    @tasks.loop(minutes=1)
    async def check_reminders(self):
        now = datetime.now()
        for reminder in self.reminders[:]:  # iterate over list
            if now >= reminder["reminder_time"]:
                user = self.bot.get_user(reminder["user"])
                channel = self.bot.get_channel(reminder["channel"])

                if user and channel:
                    embed = disnake.Embed(
                        title=f"Assignment: {reminder['name']}",
                        description=f"Due at: {reminder['due_datetime']}",
                        url="https://blackboard.sl.on.ca/ultra/calendar",
                    )
                    embed.set_author(
                        name=user.display_name,
                        icon_url=user.avatar.url if user.avatar else ""
                    )
                    await channel.send(f"{user.mention}", embed=embed)

                self.reminders.remove(reminder)  

    @check_reminders.before_loop
    async def before_check_reminders(self):
        await self.bot.wait_until_ready()  

def setup(bot):
    bot.add_cog(AssignmentReminder(bot))
