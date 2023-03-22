from flask import Flask
import datetime
from data import db_session
from data.db_session import create_session, global_init
from flask import Flask, render_template, redirect
from data.users import User
from data.jobs import Jobs
from sqlalchemy import text

db_name = input()
global_init(db_name)
db_sess = create_session()
jobs_collabs = []
leaders = []
result = []
for job in db_sess.query(Jobs):
    jobs_collabs.append(len(job.collaborators.split(', ')))
    leaders.append(job.team_leader)

for ind, el in enumerate(leaders):
    if jobs_collabs[ind] == max(jobs_collabs):
        result.append(el)

for user in db_sess.query(User).filter(User.id.in_(result)):
    print(user.name, user.surname)