# coding: utf-8
import os

from will.plugin import WillPlugin
from will.decorators import respond_to

from github import Github


class GithubTools(WillPlugin):

    def get_spicesoft(self, orgs):
        for org in orgs:
            if org.id == 7249490:
                return org
        return None

    @respond_to("liste les PR")
    def list_pr(self, message):
        g = Github(
            os.environ["GITHUB_API_LOGIN"],
            os.environ["GITHUB_API_PWD"])
        user = g.get_user()
        spicesoft = self.get_spicesoft(user.get_orgs())
        pr_txt = ""
        for repo in spicesoft.get_repos():
            for pr in repo.get_pulls():
                pr_txt += \
                    "<a href='{pr_url}'>{title}</a> - <b>repo :</b> {repo}"\
                    " - <b>user :</b> {user} - <b>status :</b> {mergeable}"\
                    "<br/>".format(
                        pr_url=pr.html_url,
                        title=pr.title,
                        repo=repo.name,
                        user=pr.user.name,
                        mergeable=pr.mergeable_state)
        self.say(pr_txt, message=message, html=True)
