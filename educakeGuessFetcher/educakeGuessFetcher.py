import requests #extrernal PIP library import

#getting URL to get questionIDs from
browserUrl=(
"https://my.educake.co.uk/my-educake/quiz/185050079"
)

splitURL=browserUrl.split("/");quizID=splitURL[-1]
urlToGoTo=f"https://my.educake.co.uk/api/student/quiz/{quizID}"

#Definied security/session headers
AUTH=(                      # MUST BE UPDATED EVRRY 30MINS below 
""
)

XSRFTOKEN=(                 #MUST BE UPDATED EVERY NEW SESSION below 
""
)

#creating headers dict
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'X-XSRF-TOKEN': XSRFTOKEN,
    'Authorization': AUTH,
}

#gets URL reponse to request
urlResponse=requests.get(urlToGoTo,headers=headers)


print(urlResponse.status_code)#give code (200 means success, 403 means JWT is probably expired, 404 is invalid quiz)
print(urlResponse.reason)#gives reason for failure

#Records text of URL
responseAsText=urlResponse.text[:3000]


#sets start and end of where to look (starts at 'questions', finishes at end of questionIDs list)
start = responseAsText.find("\"questions\":[")
end = responseAsText.find(",\"questionMap\"")

#puts into iterable list format
questionIDs=((responseAsText[start:end]).replace("\"questions\":[","")).split(",")#gets questionIDs in list form, yay!

#Getting answers, using questionIDs

baseAnswerURL="https://my.educake.co.uk/api/course/question/"

correctAnswerLUT={}
correctAnswerArr=[]

for i in range(len(questionIDs)):
    answerURL=f"{baseAnswerURL}{questionIDs[i]}/mark"

    sendPrompt={"givenAnswer" : "-1"}

    answerURLresponse=requests.post(answerURL,headers=headers,data=sendPrompt)
    answerResponseAsText=answerURLresponse.text[:2000]

    #print(answerResponseAsText)

    nstart=answerResponseAsText.find("\"correctAnswers\":[")

    nend=answerResponseAsText.find("],\"reasoning\":")

    correctAnswers=((answerResponseAsText[nstart:nend]).replace("\"correctAnswers\":[","")).replace("\"","").split(",")
    print(f"Question {i+1} answer: {correctAnswers}")

    



    


