import tkinter as tk
from tkinter import *
from tkinter import ttk
import os

root = tk.Tk()
root.minsize(600,400)

textfieldWidth = 25

#event dropdown start:

# Change the label text
def show():
    print(uid.get())

# Dropdown menu options
eventOptions = [
    "EiffelActivityCanceledEvent",
    "EiffelActivityFinishedEvent",
    "EiffelActivityStartedEvent",
    "EiffelActivityTriggeredEvent",
    "EiffelAnnouncementPublishedEvent",
    "EiffelArtifactCreatedEvent",
    "EiffelArtifactPublishedEvent",
    "EiffelArtifactReusedEvent",
    "EiffelCompositionDefinedEvent",
    "EiffelConfidenceLevelModifiedEvent",
    "EiffelEnvironmentDefinedEvent",
    "EiffelFlowContextDefinedEvent",
    "EiffelIssueDefinedEvent",
    "EiffelIssueVerifiedEvent",
    "EiffelSourceChangeCreatedEvent",
    "EiffelSourceChangeSubmittedEvent",
    "EiffelTestCaseCanceledEvent",
    "EiffelTestCaseFinishedEvent",
    "EiffelTestCaseStartedEvent",
    "EiffelTestCaseTriggeredEvent",
    "EiffelTestExecutionRecipeCollectionCreatedEvent",
    "EiffelTestSuiteFinishedEvent",
    "EiffelTestSuiteStartedEvent"
]


# datatype of menu text
eventString = StringVar()
  
# Create Label
eventLabel = Label( root , text = "Event type:" )
# event_label.pack()
eventLabel.grid(column=0,row=0)

eventDrop = OptionMenu( root , eventString , *eventOptions )
eventDrop.grid(column=0,row=1)
# event_drop.pack()

#event dropdown end

#relationship dropdown start:

# Dropdown menu options
relationshipOptions = [
    "ACTIVITY_EXECUTION",
    "ELEMENT",
    "ARTIFACT",
    "CONTEXT",
    "CAUSE",
    "COMPOSITION",
    "ENVIRONMENT",
    "CHANGE",
    "PREVIOUS_VERSION",
    "BASE",
    "SUBJECT",
    "TEST_SUITE_EXECUTION",
    "TEST_CASE_EXECUTION",
    "IUT",
]

# datatype of menu text
relationshipString = StringVar()
  
# Create Label
relationshipLabel = Label( root , text = "Relationship type:" )
relationshipLabel.grid(column=0,row=2)

relationshipDrop = OptionMenu( root , relationshipString , *relationshipOptions )
relationshipDrop.grid(column=0,row=3)
  
#relationship dropdown end

targetUidLabel = Label( root , text = "Event that caused \n the change (uid):" )
targetUidLabel.grid(column=0,row=4)

uid = tk.StringVar()

uidTextfield = ttk.Entry( root, width = textfieldWidth, textvariable = uid)
uidTextfield.grid(column=0,row=5)

userinfoLabel = Label( root , text = "User information" )
userinfoLabel.grid(column=0,row=6)

nameLabel = Label( root , text = "name:" )
nameLabel.grid(column=0,row=7)

name = tk.StringVar()

nameTextfield = ttk.Entry( root, width = textfieldWidth, textvariable = name)
nameTextfield.grid(column=0,row=8)

emailLabel = Label( root , text = "email:" )
emailLabel.grid(column=0,row=9)

email = tk.StringVar()

emailTextfield = ttk.Entry( root, width = textfieldWidth, textvariable = email)
emailTextfield.grid(column=0,row=10)

idLabel = Label( root , text = "id:" )
idLabel.grid(column=0,row=11)

userId = tk.StringVar()

idTextfield = ttk.Entry( root, width = textfieldWidth, textvariable = userId)
idTextfield.grid(column=0,row=12)

userGroupLabel = Label( root , text = "user group:" )
userGroupLabel.grid(column=0,row=13)

userGroup = tk.StringVar()

usergroupTextfield = ttk.Entry( root, width = textfieldWidth, textvariable = userGroup)
usergroupTextfield.grid(column=0,row=14)

gitLabel = Label( root , text = "git information:" )
gitLabel.grid(column=1,row=0)

commitIdLabel = Label( root , text = "commitId:" )
commitIdLabel.grid(column=1,row=1)

commitId = tk.StringVar()

commitIdTextfield = ttk.Entry( root, width = textfieldWidth, textvariable = commitId)
commitIdTextfield.grid(column=1,row=2)

branchLabel = Label( root , text = "branch:" )
branchLabel.grid(column=1,row=3)

branch = tk.StringVar()

branchTextfield = ttk.Entry( root, width = textfieldWidth, textvariable = branch)
branchTextfield.grid(column=1,row=4)

repoNameLabel = Label( root , text = "repo name:" )
repoNameLabel.grid(column=1,row=5)

repoName = tk.StringVar()

repoNameTextfield = ttk.Entry( root, width = textfieldWidth, textvariable = repoName)
repoNameTextfield.grid(column=1,row=6)

repoUriLabel = Label( root , text = "Repo uri:" )
repoUriLabel.grid(column=1,row=7)

repoUri = tk.StringVar()

repoUriTextfield = ttk.Entry( root, width = textfieldWidth, textvariable = repoUri)
repoUriTextfield.grid(column=1,row=8)

sourceLabel = Label( root , text = "Source:" )
sourceLabel.grid(column=1,row=9)

domainIdLabel = Label( root , text = "Domain id:" )
domainIdLabel.grid(column=1,row=10)

domainId = tk.StringVar()

domainIdTextfield = ttk.Entry( root, width = textfieldWidth, textvariable = domainId)
domainIdTextfield.grid(column=1,row=11)

dataLabel = Label( root , text = "Data:" )
dataLabel.grid(column=2,row=0)

def addData():
    print('addData')

addDataButton = tk.Button(root,text="Add data", command=addData)
addDataButton.grid(column=2,row=1)


def submit():
    print('submit')

submitButton = tk.Button(root,text="Submit", command=submit)
submitButton.grid(column=1,row=17)



root.mainloop()

print('Hello')