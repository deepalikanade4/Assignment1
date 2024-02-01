
# comand to run = python Assignment1.py 'C:\Users\Readchilly_task\Assignment1\Userdata.csv'
# pls give path for csv file



import argparse     #read input from cmdline
import csv          
import json
import datetime     #used for get current date

class JsonWriter:
    
    # thid 'readfile_to_json' function read csv file and parse data to json format and save file in same project folder

    def readfile_to_json(csvfile):
        Usersdata=list()
    
        with open(csvfile,'r') as f:
            f_read=csv.DictReader(f)
            
            for line in f_read:
                Userdata={}
                Userdata['ID']=int(line['ID'])
                Userdata['Username']=line['Username']
                Userdata['Email']=line['Email']
                Userdata['Designation']=line['Designation']
                               
                Usersdata.append(Userdata)
                
        # following code to formate  name of file as user_information_CURRENT_DATE
        user_information_CURRENT_DATE="User_information_{0}.json".format(datetime.date.today())

        # create json file and writes data in it
        with open(user_information_CURRENT_DATE,'w') as json_f:

            json.dump(Usersdata,json_f,indent=1)


if __name__== '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--csv_path',type=str) #taking argument named as --csv_path from user
    args=parser.parse_args()
    
    # creating instance of class and calling function by passing file path as argument for read and write
    jsonwriter=JsonWriter() 
    jsonwriter.readfile_to_json(args.csv_path)
   
