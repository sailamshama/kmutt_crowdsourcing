import boto3

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

mturk = boto3.client(
	#seems like mandatory parameter
	service_name = 'mturk',

	#set this to use sandbox or live account
	endpoint_url = MTURK_SANDBOX
)

#uncomment to check if using the right account
#pmmxrint(mturk.get_account_balance()['AvailableBalance'])

question = open('/Users/saila/Desktop/Environments/aws_env/implementation/questions.xml').read()

new_hit = mturk.create_hit(
	Title = 'Is this Tweet happy, angry, excited, scared, annoyed or upset?',
	Description = 'Read this tweet and type out one word to describe the emotion of the person posting it: happy, angry, scared, annoyed or upset',
	Keywords = 'text, quick, labeling',
	Reward = '0.15', 
	MaxAssignments = 1, 
	LifetimeInSeconds = 172800, 
	AssignmentDurationInSeconds = 600, 
	AutoApprovalDelayInSeconds = 14400,
	Question = question,
)

print("A new HIT has been created. You can preview it here:")
print("https://workersandbox.mturk.com/mturk/preview?groupId="+new_hit['HIT']['HITGroupId'])


