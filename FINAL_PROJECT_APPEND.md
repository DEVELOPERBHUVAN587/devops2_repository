![street view with city buildings, market and street
sings](media/image1.jpeg){width="8.4875in" height="7.309722222222222in"}

+-----------------------------------------------------------------------+
|                                                                       |
+-----------------------------------------------------------------------+
|                                                                       |
+-----------------------------------------------------------------------+
| JULY 3                                                                |
|                                                                       |
| Email id: vishnu.23bce7518@vitapstudent.ac.in                         |
|                                                                       |
| 23BCE7518                                                             |
|                                                                       |
| Authored by: [P L V BHUVAN\                                           |
| https://github.com/DEVELOPERBHUVAN587/devops2_repository]{.underline} |
+-----------------------------------------------------------------------+

![logo-placeholder](media/image2.png){width="1.6229166666666666in"
height="0.7041666666666667in"}![white rectangle for text on
cover](media/image4.jpeg){width="4.307638888888889in"
height="9.041666666666666in"}

# Email-Verification-game 📨🕹️

+-----------------------------------------------------------------------+
| ## USING PYGA                                                         |
| ME ![](media/image5.jpeg){width="6.9in" height="5.040972222222222in"} |
|                                                                       |
| 🎯 Project Overview                                                   |
|                                                                       |
| Email Game is an interactive Python-based quiz application designed   |
| to test users on identifying valid and invalid email formats. Built   |
| with pygame, it features an intuitive graphical interface and         |
| engaging sound effects to make learning fun and effective.            |
|                                                                       |
| Want to insert a picture from your files or add a shape, text box, or |
| table? You got it! On the Insert tab of the ribbon, just tap the      |
| option you need.                                                      |
+-----------------------------------------------------------------------+
|                                                                       |
+-----------------------------------------------------------------------+
| The project demonstrates a full DevOps pipeline by integrating:       |
|                                                                       |
| -   CI/CD using Jenkins and GitHub Actions                            |
|                                                                       |
| -   Infrastructure provisioning via Terraform                         |
|                                                                       |
| -   Configuration management with Puppet                              |
|                                                                       |
| -   Monitoring and metrics via Prometheus + Grafana                   |
|                                                                       |
| This end-to-end pipeline provisions a VM, deploys the game,           |
| auto-starts it, and exposes performance and gameplay metrics---all    |
| automatically.                                                        |
|                                                                       |
| Want to insert a picture from your files or add a shape, text box, or |
| table? You got it! On the Insert tab of the ribbon, just tap the      |
| option you need.                                                      |
|                                                                       |
| *\                                                                    |
| STEP1: INSTALLING AN PYTHON ENVIRONMENT\                              |
| *\$ snap find "pycharm"\                                              |
| *\                                                                    |
| *![](media/image6.jpeg){width="6.9in" height="1.5305555555555554in"}  |
+-----------------------------------------------------------------------+

![](media/image7.jpeg){width="6.927777777777778in"
height="3.0833333333333335in"}

🛠️ PyCharm Community Edition -- Python IDE for Everyone

PyCharm Community Edition, developed by JetBrains, is a powerful
open-source integrated development environment (IDE) for Python.

We will be using community edition for building our game.\
\$ sudo snap install pycharm-community --classic\
this command will install our pycharm ide\
![](media/image8.jpeg){width="6.9in" height="0.9666666666666667in"}\
\
Now, we have launched our app\
![](media/image9.jpeg){width="3.375in" height="2.8041666666666667in"}\
\
Opening Pycharm,We will accept the agreement\
![](media/image10.jpeg){width="4.027777777777778in"
height="2.0833333333333335in"}

*STEP2: CREATING A NEW PYTHON PROJECT IN PYCHARM\
\
*![](media/image11.jpeg){width="5.368055555555555in"
height="4.2945527121609794in"}*\
*After this select the name of your project and using an existing
virtual environment for the game.*\
Click on Save it will open an interface for you.\
*![](media/image12.jpeg){width="4.694444444444445in"
height="3.007732939632546in"}

Now we will be installing pytest in the pycharm terminal which is
similar to maven where we will test our software applications and
dependencies.\
\$ pip install pytest requests python-dotenv\
\
![](media/image13.jpeg){width="6.9in" height="1.6666666666666667in"}\
\
we will also build python dependencies for our game.\
![](media/image14.jpeg){width="6.9in" height="1.5715277777777779in"}\
\
Next, We should a build a proper folder structure for our game\
![](media/image15.png){width="3.981955380577428in"
height="3.6912368766404198in"}\
This are the required files needed and code scripts needed for game
application\
![](media/image16.png){width="3.627198162729659in"
height="4.121499343832021in"}\
\
This is the main python code for our game application\
![](media/image17.png){width="6.109458661417323in"
height="3.935239501312336in"}

we will also make code for to test our dependencies in pycharm in tests
folder\
*\
*![](media/image18.jpeg){width="5.902777777777778in"
height="3.8122484689413825in"}*\
\
confest.py file\
*![](media/image19.jpeg){width="5.611111111111111in"
height="4.080555555555556in"}

*\
also to test our core functionality of the game we will add a
tests_main.py file\
*![](media/image20.jpeg){width="4.534722222222222in"
height="4.190146544181977in"}*\
\
pkgdata.py where it has all the imported packages\
*![](media/image21.png){width="4.546662292213473in"
height="3.991599956255468in"}

now we are going to add our requirments.txt which is the dependencies
file by adding a local python interpreter\
![](media/image22.jpeg){width="6.9in" height="3.925in"}\
\
now we select on existing interpreter\
![](media/image23.jpeg){width="5.903324584426946in"
height="4.166666666666667in"}

Go to python interpreter in the above image and click on on add local
repository\
now this will add a dependencies file named as requirements.txt in the
project folder\
![](media/image24.jpeg){width="4.486111111111111in"
height="4.1082042869641295in"}\
\
Now, for our game we will add the sound affects which I have downloaded
and will prompt it to chatgpt to convert this into .wav file for correct
and incorrect answers\
\
![](media/image25.png){width="6.9in" height="3.073611111111111in"}\
now we will convert this into .wav using chatgpt and we will download
from the gpt in our vm ware\
![](media/image26.png){width="6.9in" height="2.8208333333333333in"}\
\
and after downloading the sound file check if the folder is setup in the
files\
![](media/image27.png){width="3.771359361329834in"
height="1.5627176290463691in"}\
Add this audio files into our python project\
![](media/image28.jpeg){width="4.188611111111111in" height="3.1875in"}

Incorrect.wav\
![](media/image29.jpeg){width="4.145833333333333in"
height="3.1619247594050743in"}\
\
background music.mp3(death note theme song)\
![](media/image30.jpeg){width="4.451388888888889in"
height="3.1821872265966755in"}

*STEP 3: TESTING THE DEPENDENCIES AND RUNNING OTHER FILES*\
\$ PYTEST\
![](media/image31.png){width="6.9in" height="2.10625in"}\
\
running our test_dependency file\
\
![](media/image32.jpeg){width="5.409722222222222in"
height="3.384342738407699in"}\
\
Running our game application\
![](media/image33.png){width="5.190949256342957in"
height="3.059922353455818in"}\
\
We have to identify whether the mail is real or fake and we have 5
rounds which has 5 different types of emails\
![](media/image34.jpeg){width="5.222222222222222in"
height="3.920871609798775in"}\
\
![](media/image35.png){width="4.3125in" height="3.3858508311461066in"}\
it's showing a phishing mail\
but while playing this game by the sound effects we will be able to
identify if our answer is correct or not\
![](media/image36.png){width="6.192420166229222in"
height="4.687941819772528in"}\
it's showing a legitimate email\
but while playing this game by the sound effects we will be able to
identify if our answer is correct or not\
![](media/image37.png){width="5.388888888888889in" height="3.075in"}\
\
this is our final score of the game and the game will also give feedback
based on the score.\
\
![](media/image38.jpeg){width="4.5625in" height="3.8250426509186353in"}\
after click on quit and the game is over\
\
pkgdata.py\
![](media/image39.jpeg){width="6.9in" height="4.253472222222222in"}\
![](media/image40.jpeg){width="6.9in" height="1.2229166666666667in"}\
\
now here is our project files\
![](media/image41.png){width="5.398529090113736in"
height="2.581541994750656in"}\
\
Step5: Running the game on terminal and cloning of our project\
 initially attempted to run the 3D Email Verification Game but
encountered technical limitations on my Ubuntu virtual machine (VM). Due
to missing dependencies or hardware constraints (detailed below), I
switched to the 2D version to complete the exercise without
interruption.

Why the 3D Version Didn't Run:

The 3D game likely requires:

1.  Hardware Acceleration:

    -   A VM often lacks direct access to the host's GPU, which is
        critical for 3D rendering.

    -   Ensure VirtualBox/VMWare is configured with 3D acceleration
        enabled (e.g., in VM settings \> Display \> Enable 3D
        Acceleration).

2.  Dependencies on Ubuntu:

    -   OpenGL/Mesa Drivers:

sudo apt install mesa-utils libgl1-mesa-glx

-   Vulkan (for advanced 3D):

sudo apt install vulkan-tools

-   Graphics Stack:

sudo apt install xorg-dev\
\
So I will be using 2d-version of the game for building the ci/cd
pipeline using jenkins.\
Now,let's run our game in the ubuntu terminal\
![](media/image42.png){width="4.819970472440945in"
height="2.9668821084864394in"}

Now, we will be creating a devops2_repository for our project so that we
can build a separate dockerfiles and jenkinsfiles,etc separately from
the python project\
\
First I have created a repo in the github\
![](media/image43.jpeg){width="6.9in" height="2.8354166666666667in"}\
![](media/image44.jpeg){width="6.9in" height="3.0909722222222222in"}\
\
now I am going to perform these steps to add my devops2_repository in my
ubuntu vm as a local git folder\
\
![](media/image45.png){width="2.4097222222222223in"
height="1.761111111111111in"}\
\
![](media/image46.jpeg){width="6.9in" height="3.90625in"}\
\
after doing the above steps our devops2_repository is added in the local
vm\
Now, we will clone our pythonproject with our devops2_repository\
![](media/image47.jpeg){width="2.5972222222222223in"
height="3.683043525809274in"}\
\
![](media/image48.jpeg){width="4.701388888888889in"
height="1.7708333333333333in"}\
\
![](media/image49.jpeg){width="3.8541666666666665in"
height="2.643279746281715in"}\
\
after doing these steps we will clone with our new repo\
![](media/image50.jpeg){width="6.9in" height="1.7569444444444444in"}\
we will also use PAT for the password\
![](media/image51.jpeg){width="6.9in" height="3.9715277777777778in"}\
Now,we will check whether all the files are copied in the
devops2_repository\
![](media/image52.png){width="6.9in" height="2.352777777777778in"}\
\
\
We have to make sure there is different origin remote set for our python
project and our devops2_repository\
![](media/image53.jpeg){width="4.381944444444445in"
height="2.978627515310586in"}\
![](media/image54.jpeg){width="4.673611111111111in"
height="3.146784776902887in"}\
after we have set this remote we will check if the origin is maintained
separately for devops2_repository or not\
![](media/image55.jpeg){width="6.9in" height="0.8590277777777777in"}\
\
Now,we to create a proper folder structure for our devops2_repository\
as in the below image\
\
![](media/image56.png){width="5.4118569553805775in"
height="2.7838178040244967in"}\
\
\
*STEP6: DOCKERZIATION USING DOCKER FOR THE GAME*\
\
now we have to build a Dockerfile in our devops2_repository\
before that I will creating a docker directory under devops2_repository\
![](media/image57.png){width="6.9in" height="0.2611111111111111in"}\
\
after this will add my Dockerfile for the building the game\
\$ cd docker\
\$ sudo nano Dockerfile\
![](media/image58.png){width="6.9in" height="0.33611111111111114in"}\
\
the code contents of the Dockerfile\
![](media/image59.png){width="6.9in" height="4.294444444444444in"}\
\
Now, building our game using the docker container\
![](media/image60.jpeg){width="6.9in" height="2.5868055555555554in"}\
As we have successfully built docker container we will run our docker
container whether our game is successfully working or not for that we
have to install pulse audio\
\$ sudo apt install pulseaudio\
![](media/image61.png){width="6.9in" height="1.1319444444444444in"}\
\
![](media/image62.jpeg){width="6.9in" height="1.979861111111111in"}

Now we have successfully runned our game in the docker container\
\
we will also check whether docker image is created or not\
![](media/image63.png){width="6.9in" height="1.0104166666666667in"}\
\
*STEP7: CREATING A CI/CD PIPELINE USING JENKINS*\
\
Now we will create a JenkinsFile in our devops2_repository\
and we will push this file to our github too\
\
![](media/image64.png){width="6.9in" height="0.3597222222222222in"}\
\
![](media/image65.jpeg){width="6.9in" height="3.7270833333333333in"}\
\
![](media/image66.jpeg){width="6.923611111111111in"
height="3.4097222222222223in"}\
\
Now go to Jenkins and give the name for the pipeline\
![](media/image67.png){width="6.9in" height="3.7111111111111112in"}\
after that we will add our github repository url here which configures
Jenkins in building the pipeline\
\
Linking the local repository on the \@git user of the virtual machine\
![](media/image68.png){width="6.9in" height="3.660416666666667in"}\
after these changes add a script path as the Jenkinsfile for smooth run\
![](media/image69.png){width="6.9in" height="3.6534722222222222in"}\
click on save and your pipeline is setup\
![](media/image70.png){width="6.9in" height="3.203472222222222in"}\
click on build now and verify the console output and the pipeline
overview\
![](media/image71.jpeg){width="6.277777777777778in"
height="3.8774890638670167in"}\
successfully we have setup CI using Jenkins\
![](media/image72.jpeg){width="6.9in" height="4.025in"}\
![](media/image73.png){width="6.9in" height="3.560416666666667in"}\
\
we have also successfully runned our game\
![](media/image74.jpeg){width="6.9in" height="4.103472222222222in"}\
\
![](media/image75.jpeg){width="6.9in" height="3.5520833333333335in"}\
we have Successful deployment using Jenkins which is triggered on push
to \@main branch of the local git repository\
\
now we can also check out the timings of the Pipeline too\
![](media/image76.jpeg){width="6.9in" height="3.6243055555555554in"}\
\
![](media/image77.jpeg){width="6.180555555555555in"
height="4.558284120734908in"}\
\
![](media/image78.jpeg){width="6.222222222222222in"
height="4.271515748031496in"}\
*STEP8: TERRAFORM SETUP*\
✅ Why We Used Terraform

1.  Automated VM Provisioning:

    -   Terraform was used to create a single KVM-based local virtual
        machine automatically.

    -   This saved us from manually creating the VM using virt-manager
        or virsh.

Now we have create a directory terraform in inside the
devops2_repository and we will add required files for it\
![](media/image79.png){width="6.9in" height="0.2361111111111111in"}\
we will add file structure in this format\
![](media/image80.png){width="6.9in" height="1.8979166666666667in"}\
\
now we will add code contents in our terraform files .tf\
\$ sudo nano main.tf\
![](media/image81.png){width="6.9in" height="0.7298611111111111in"}\
\
![](media/image82.jpeg){width="5.173611111111111in"
height="2.747700131233596in"}\
![](media/image83.jpeg){width="5.368055555555555in"
height="3.192956036745407in"}\
\
\$ sudo nano variables.tf\
\
![](media/image84.jpeg){width="6.9in" height="1.5840277777777778in"}\
\
\$ sudo nano outputs.tf\
![](media/image85.jpeg){width="6.9in" height="1.773611111111111in"}\
\
\
\
\
\
Next, we will perform terraform init\
![](media/image86.jpeg){width="6.9in" height="3.0652777777777778in"}\
\
we will also install virsh so that there will be no obstacles for
terraform apply step\
\
\$ virsh pool-define-as default dir \-\-\--"var/lib/libvirt/images"\
![](media/image87.jpeg){width="6.9in" height="3.3583333333333334in"}\
\$ virsh pool-list\
![](media/image88.png){width="6.9in" height="0.7486111111111111in"}\
\
Now perform terraform apply\
![](media/image89.jpeg){width="6.9in" height="3.5375in"}\
\
![](media/image90.jpeg){width="6.9in" height="2.995833333333333in"}\
\
Thefore we have successfully setup a local vm machine for our game to
deploy now we will deploy our game using puppet\
\
*STEP 9:  SETTING THE DEPLOYMENT OF THE PUPPET*

We will create a directory for puppet which has manifests file and and
the files of our game\
![](media/image91.jpeg){width="6.9in" height="0.3388888888888889in"}\
we are going to do standalone puppet setup instead of master and agent
for that we will need a init.pp file for deploying our game\
\
before the adding the code contents in the init.pp\
we should create a proper directory structure for our puppet\
\
deployment/puppet/

├── manifests/

│ └── init.pp

├── files/

│ ├── main.py

│ ├── requirements.txt

│ └── assets/

│ ├── background_music.mp3

│ ├── correct.wav

│ └── incorrect.wav\
after this we should copy all the files of our project for deployment\
![](media/image92.jpeg){width="6.9in" height="1.05in"}

![](media/image93.png){width="4.961730096237971in"
height="1.5415529308836395in"}\
\
we successfully setup a proper directory now we are going to add the
code contents in the init.pp\
![](media/image94.jpeg){width="6.9in" height="3.3513888888888888in"}\
\
![](media/image95.jpeg){width="4.104166666666667in"
height="2.223611111111111in"}\
![](media/image96.jpeg){width="6.9in" height="2.779166666666667in"}\
\
\$ sudo /opt/puppetlabs/bin/puppet apply \\ \--modulepath=./ \\\
![](media/image97.jpeg){width="6.9in" height="0.7291666666666666in"}\
\
we have successfully applied our puppet file\
![](media/image98.png){width="6.9in" height="1.3076388888888888in"}\
\
\
after setting up we will check if our game is deployed or not\
![](media/image99.png){width="6.9in" height="1.0131944444444445in"}\
\
![](media/image100.png){width="6.9in" height="4.06875in"}\
![](media/image101.png){width="6.9in" height="4.254861111111111in"}\
this says that our project is in the home directory which have been
successfully deployed\
\
*STEP 10:  SETTING UP PROMETHEUS AND GRAFAN FOR MONITORING THE USAGE AND
SHOWING THE STASTICS OF THE EMAIL-GAME*\
\
First we will create a directory name monitoring for our game in the
devops2_repository\
![](media/image102.jpeg){width="6.9in" height="0.21944444444444444in"}\
\
after that we should create file structure in the directory monitoring\
![](media/image103.png){width="6.9in" height="0.6180555555555556in"}\
\
now our monitoring directory strcture should look like this\
![](media/image104.jpeg){width="6.9in" height="2.7743055555555554in"}\
\
now after creating this file structure we should add our code contents
in each file\
\
\$ sudo nano docker-compose.yml\
![](media/image105.jpeg){width="6.9in" height="4.452083333333333in"}\
![](media/image106.jpeg){width="6.9in" height="1.5763888888888888in"}\
\
\$ sudo nano Prometheus/Prometheus.yml\
![](media/image107.jpeg){width="5.3125in" height="2.562357830271216in"}\
\
also we will add our requirments.txt file in the Grafana\
![](media/image108.jpeg){width="6.9in" height="3.7291666666666665in"}\
![](media/image109.jpeg){width="6.9in" height="3.902083333333333in"}\
\
![](media/image110.jpeg){width="6.9in" height="3.1125in"}\
\
at last we will do \$ docker compose up -d\
![](media/image111.jpeg){width="6.9in" height="0.7958333333333333in"}\
\
\
\
we will got our Grafana and will start our Prometheus:
[http://localhost:3000/]{.underline}

![](media/image112.png){width="6.9in" height="3.438888888888889in"}\
\
Go to data sources and add Prometheus for testing metrics\
![](media/image113.png){width="6.9in" height="3.816666666666667in"}\
\
add the Prometheus data source and configure the settings accordingly\
![](media/image114.png){width="6.9in" height="3.826388888888889in"}\
after this you can you see your Prometheus in the data sources and click
on build a dashboard and create one in the node 1860\
\
![](media/image115.png){width="6.9in" height="3.813888888888889in"}\
\
![](media/image116.png){width="6.9in" height="3.8in"}\
\
now your dashboard is created\
![](media/image117.png){width="6.9in" height="4.113194444444445in"}\
\
as you can see our node exporter full dashboard

![](media/image118.png){width="6.9in" height="3.814583333333333in"}\
you have successfully started Prometheus but now we have to run the
Prometheus server by following few commands\
\
\$ wget
https://github.com/prometheus/node_exporter/releases/download/v1.8.1/node_exporter-1.8.1.linux-amd64.tar.gz\
![](media/image119.jpeg){width="6.9in" height="3.402083333333333in"}\
This command downloads the Node Exporter binary for Linux (64-bit
architecture) version 1.8.1.\
\
\
\$ tar -xvzf
node_exporter-1.8.1.linux-amd64.tar.gz![](media/image120.jpeg){width="6.9in"
height="0.8472222222222222in"}\
This command:

-   x: extracts the contents

-   v: shows a verbose listing of files as they are extracted

-   z: handles gzip-compressed files

-   f: refers to the filename to extract

![](media/image121.jpeg){width="6.9in" height="0.29444444444444445in"}\
This changes the current working directory to the extracted Node
Exporter folder, allowing the user to run or manage the executable and
related files.

\$ ./node-exporter\
![](media/image122.jpeg){width="5.361111111111111in"
height="2.3229166666666665in"}\
\
\
The Node Exporter is a Prometheus exporter for hardware and OS metrics
exposed by \*nix kernels. It is commonly used in monitoring setups to
collect system-level metrics such as CPU, memory, disk, and network
usage.\
\
\
now we should do docker compose up -d again to see if Prometheus running
or not\
![](media/image123.png){width="6.9in" height="0.9583333333333334in"}\
\
we have successfully runned our Prometheus\
now we will test our metrics at 192.168.122.1\
![](media/image124.jpeg){width="6.9in" height="4.440277777777778in"}\
\
this monitors our CPU BASIC AND MEMORY BASIC\
![](media/image125.jpeg){width="6.9in" height="3.797222222222222in"}\
\
now to test our email-game metrics we will create a new dashboard and
add JSON file\
for it\
![](media/image126.jpeg){width="6.9in" height="3.8354166666666667in"}
![](media/image127.jpeg){width="6.9in" height="3.7597222222222224in"}\
\
now we configured our settings for the email-game

![](media/image128.jpeg){width="6.9in" height="3.8854166666666665in"}\
\
we have successfully created a dashboard now we will check whether our
game is\
working or not\
![](media/image129.jpeg){width="5.256944444444445in"
height="3.278183508311461in"}\
![](media/image130.jpeg){width="5.298611111111111in"
height="3.341494969378828in"}\
![](media/image131.jpeg){width="5.069444444444445in"
height="2.4881944444444444in"}\
we will use this command which will setup an virtual server so that we
can test the metrics for our game\
![](media/image132.jpeg){width="6.9in" height="3.9652777777777777in"}\
now we can see our game now after playing game we should see if it
recorded the metrics or not\
![](media/image133.jpeg){width="6.723985126859143in" height="3.6875in"}\
![](media/image134.png){width="6.9in" height="3.841666666666667in"}\
see as I have completed my game I have gotten the metrics which shows
that our game monitoring setups\
![](media/image135.jpeg){width="6.9in" height="3.9069444444444446in"}\
we can view the metrics for all the type of answers\
![](media/image136.jpeg){width="6.9in" height="3.8534722222222224in"}\
\
![](media/image137.jpeg){width="6.9in" height="3.6729166666666666in"}\
![](media/image138.png){width="6.9in" height="3.6006944444444446in"}\
metrics for game played\
![](media/image139.png){width="6.9in" height="3.81875in"}\
metrics for correct answers\
![](media/image140.png){width="6.9in" height="3.8541666666666665in"}\
metrics for incorrect answers\
![](media/image141.png){width="6.785889107611548in"
height="2.952435476815398in"}\
\
this is our devops2_repository in github\
<https://github.com/DEVELOPERBHUVAN587/devops2_repository>[\
here is my entire project]{.underline}
