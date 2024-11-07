import disnake
from disnake.ext import commands, tasks
from datetime import datetime, timedelta

class AssignmentReminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminders = []  
        self.check_reminders.start()

    @commands.slash_command(description="Set a reminder for an assignment")
    async def remind(
        self,
        interaction: disnake.ApplicationCommandInteraction,
        name: str,
        due_date: str  # format: YYYY-MM-DD HH:MM
    ):
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d %H:%M")
            reminder_time = due_date_obj - timedelta(hours=2)  # set reminder 2 hours before so we dont pull a blackboard
        except ValueError:
            await interaction.response.send_message("Invalid date format. Use `YYYY-MM-DD HH:MM`.")
            return

        # add the reminder to the list
        self.reminders.append({
            "user": interaction.author.id,
            "channel": interaction.channel_id,
            "name": name,
            "due_date": due_date_obj,
            "reminder_time": reminder_time
        })

        await interaction.response.send_message(f"Reminder set for assignment '{name}' due on {due_date_obj}.")

    @tasks.loop(minutes=1)
    async def check_reminders(self):
        now = datetime.now()
        for reminder in self.reminders[:]:  #iterate over list
            if now >= reminder["reminder_time"]:
                user = self.bot.get_user(reminder["user"])
                channel = self.bot.get_channel(reminder["channel"])

                if user and channel:
                    await channel.send(
                        f"{user.mention}, remember your assignment '{reminder['name']}' is due at {reminder['due_date']}!"
                    )

                self.reminders.remove(reminder)  

    @check_reminders.before_loop
    async def before_check_reminders(self):
        await self.bot.wait_until_ready() 

def setup(bot):
    bot.add_cog(AssignmentReminder(bot))