#!/usr/bin/python3
import argparse
import os
import sys
import requests
import json

SMMRY_API_KEY='9E46BEF0A6'
SMMRY_URL='https://api.smmry.com/'

def summarizeText(text):
    url=SMMRY_URL+'&SM_API_KEY='+SMMRY_API_KEY
    headers={
    'Expect':''
    }
    response=requests.post(url, data={'sm_api_input':text}, headers=headers)
    summary=json.loads(response.content.decode('utf-8'))
    return summary

def summarizeFile(file):
    print("Input file is: {}".format(args.ifile.name))
    fileText=args.ifile.read()
    return summarizeText(fileText)

def summarizeURL(url):
    print("URL to summarize is: {}".format(args.url))
    url=SMMRY_URL+'&SM_API_KEY='+SMMRY_API_KEY+'&SM_URL='+args.url
    response=requests.get(url)
    summary=json.loads(response.content.decode('utf-8'))
    return summary

def summarizeStdin():
    inp=input("Using standard input for summary. Type the text you want to summarize:")
    return summarizeText(inp)

parser = argparse.ArgumentParser()
group=parser.add_mutually_exclusive_group()
group.add_argument('-i', '--ifile', type=argparse.FileType('r'), help='Input file to summarize')
group.add_argument('-u', '--url', help='URL of page to summarize')
parser.add_argument('-o', '--ofile', type=argparse.FileType('w', encoding='UTF-8'), help='Output file')

args = parser.parse_args()
if args.ifile:
    summary=summarizeFile(args.ifile)
elif args.url:
    summary=summarizeURL(args.url)
else:
    summary=summarizeStdin()
if args.ofile:
    print("Summary was written to: {}".format(args.ofile.name))
    args.ofile.write(summary)
else:
    print("The summarized text is:\n{}".format(summary))
