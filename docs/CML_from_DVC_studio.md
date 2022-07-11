Step 1: Sign in with your Github Account

Step 2: Click on 'Add View' button

Step 3: Integrate your Github with DVC Studio and select your DVC repository for which you want to create a view

Step 4: Once the repo gets added in your DVC Studio account, click 'Connect'

Step 5: Configure settings:
 - Project directory for the view
 - Data remotes/cloud storage
 - Custom metrics and parameters

Step 6 : A new View gets added to your DVC Studio account dashboard. The dashboard contains many functionalities. You can explore.

## You can also run the experiments directly from DVC Studio.

Step 1: Copy paste ci-cd.yml file from [link][(https://cml.dev/) website for DVC under GitHub

Step 2: Add Github token

- To add toekn, in your github account , go to setting->Developer setting->Personal access token.
- Generate new token
- Give basic read/write access

Step 3: To add github toekn to your current repo
- Got your current repository ->Settings->Secrets->Actions
- Click on new repository secret
- Give the name to the new secret which you mentioned in **ci-cd.yml** and paste the token value

Step 7: Push all your changes of ci-cd.yml

Step 8: Go to Github Actions of your repo.

Setp 9: You can see the reports.md file as a commnet in your github commit 

Setp 10: Congrats! your Github workflowws is integrated with your DVC studio.

Now you can directly do diffent experiments(Runs) from DVC Studio itself.
