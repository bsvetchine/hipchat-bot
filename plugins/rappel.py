# coding: utf-8
import datetime
from will.plugin import WillPlugin
from will.decorators import respond_to


class ReminderPlugin(WillPlugin):

    @respond_to(
        u"rappelle moi (?P<reminder_text>.*?) (à|a) (?P<remind_time>.*)")
    def remind_me_at(self, message, reminder_text=None, remind_time=None):
        """Set a reminder for a thing, at a time."""
        now = datetime.datetime.now()
        parsed_time = self.parse_natural_time(remind_time)
        natural_datetime = self.to_natural_day_and_time(parsed_time)

        formatted_reminder_text = u"@%(from_handle)s, tu m'as demandé de te rappeller %(reminder_text)s" % {
            "from_handle": message.sender.nick,
            "reminder_text": reminder_text,
        }
        self.schedule_say(formatted_reminder_text, parsed_time,
                          message=message)
        self.say("%(reminder_text)s %(natural_datetime)s. Got it." % locals(),
                 message=message)
