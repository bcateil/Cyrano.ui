import json
import requests
import cgi


form = cgi.FieldStorage()

searchterm = form.getvalue('cyranoInput')

print(searchterm)

# "http://color-demo-api.cyrano.ai/bag_of_words"

# "http://color-demo-api.cyrano.ai/chat/$_model"

headers1 = {"Content-Type": "application/json", "Accept": "text/plain"}

body = {"message": "This evening, members of our community gathered on campus to honor Noah Domingo, a first-year member of the Anteater family, who died after a party nearly two weeks ago."
                   "We remain shocked and saddened by Noah’s tragic death. We won’t know exactly why he died for several more weeks, following investigations that will proceed in accordance with all considerations of fairness and due process. Yet many of us are reflecting on the larger question: What else can we do to prevent another such tragedy?"
                   "Based on what we know today, large amounts of alcohol were consumed at the party Noah attended. Underage drinking is a concern at most college campuses; UCI is no exception. We invest heavily in activities designed to educate our students and their leaders about alcohol and drug abuse, as well as the negative behaviors that result, such as sexual violence. Our mandatory training, along with a multitude of orientations and workshops, seem to be beneficial, as we have fewer incidences of alcohol and drug abuse than the national average and most of our peers."
                   "But we should hold ourselves to a higher standard. Prevention and policing bad behavior isn’t enough. We must be committed to fostering an ethos of mutual care and whole-person wellness."
                   "In that spirit, last year we launched our Healthy Campus Initiative, dedicated to working with community and national leaders to study risky behaviors, identify improvements and sustain a healthy campus life. While the scope of this effort is broad, Noah’s death brings an urgent focus on alcohol and substance abuse, from the cultural pressures that encourage unhealthy behavior to the policies designed to mitigate danger. Our Interfraternity Council is already taking steps to examine this issue, with the goal of improving the health and wellness of its members, and I applaud their initial efforts. But this responsibility should not rest on their shoulders alone."
                   "Therefore, I am directing Interim Vice Chancellor of Student Affairs Edgar Dormitorio to assemble a team consisting of students, faculty, and staff to review and report on (a) our current campus culture, (b) our existing efforts toward promoting health and preventing abuse, and (c) recommendations for how we might improve our culture and policies based on new research, best practices, and our aspirations to ensure a healthier environment in the future."
                   "We will announce members of this team by the end of the month. They will be charged with consulting and collecting input from a broad range of constituents and experts, with final findings and recommendations due to me by April 15."
                   "In memory of Noah, let us work toward a future in which we all benefit from an enhanced culture of self care, mutual care, bystander intervention, and whole-person wellness – a future in which we are allowed to continuously shine brighter."}

input = json.dumps(body)


#Dictionary of Dimension : weights (sum) that appear in the Bags
test_dict = {}



#authKey = "A7BB481E40C7EC70AB255B3991186C382F471BC19DDC31D3FD55FC8E8439DBE8"

headers2 = {"auth_key":
          "A7BB481E40C7EC70AB255B3991186C382F471BC19DDC31D3FD55FC8E8439DBE8"}




# response = requests.get("http://color-demo-api.cyrano.ai/bag_of_words", headers = headers2)

# json_data1 = json.loads(response.text)

# json_data1.get("data")[3] == Sensory Bag                      5be8d6d8fd4f43000c7782dd
# json_data1.get("data")[10] == Motivation and Commitment Bag   5c2547b2fd4f43000f2ce3e1




# Get the data from the Senses/Sensory Bag
SensoryCheck = requests.post("http://color-demo-api.cyrano.ai/chat/5be8f3e8fd4f43000c778398", data = input, headers = headers1)

print(SensoryCheck.status_code)

json_data = json.loads(SensoryCheck.text)

SensoryData = json_data.get("data")



#Get the data from the Commitment and Motivation Bag
CommotiveCheck = requests.post("http://color-demo-api.cyrano.ai/chat/5c2547b2fd4f43000f2ce3e1", data = input, headers = headers1)


# print(CommotiveCheck.status_code)

json_data = json.loads(CommotiveCheck.text)

CommotiveData = json_data.get("data")



# Get the weights of the words found in the Senses/Sensory Bag
for word in SensoryData:
    if word.get("found") == True:
        if word.get("dimensions") in test_dict:
            test_dict[word.get("dimensions")] += word.get("weight")
        else:
            test_dict[word.get("dimensions")] = word.get("weight")

# Get weights of the words found in the Commitment and Motivation bag
for word in CommotiveData:
    if word.get("found") == True:
        if word.get("dimensions") in test_dict:
            test_dict[word.get("dimensions")] += word.get("weight")
        else:
            test_dict[word.get("dimensions")] = word.get("weight")




# The following section normalizes the numbers to work with numbers between 0 and 1

highest = max(test_dict, key = test_dict.get)

divideBy = test_dict[highest]

for i in test_dict:
    test_dict[i] = test_dict[i]/divideBy







