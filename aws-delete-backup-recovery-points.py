import boto3
import os
import xlrd
import xlwt

session = boto3.Session(profile_name='ops')
client = session.client("backup")

vault = 'EBS-Prod'
region = 'us-west-2'
bookPath = input("Enter the workbook's absolute path - ")
sheetName = input("Enter the name of the sheet in the workbook - ")
columnNumber = int(
    input("Enter the Column Number of the id , 0 being the first column - "))

workbook = xlrd.open_workbook(bookPath)
worksheet = workbook.sheet_by_name(sheetName)

for row in range(worksheet.nrows):
    if (row != 0):
        id = worksheet.cell(row, columnNumber).value
        arn = ''
        if id.startswith('ami'):
            arn = 'arn:aws:ec2:'+region+'::image/'+id
        elif id.startswith('snap'):
            arn = 'arn:aws:ec2:'+region+'::snapshot/'+id
        else:
            print('invalid id')

        print(arn)
        
        try:
            client.delete_recovery_point(
                BackupVaultName=vault,
                RecoveryPointArn=arn
            )
        except:
            print(arn+" already deleted / not found")