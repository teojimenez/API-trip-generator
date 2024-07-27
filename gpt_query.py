from openai import OpenAI
from dotenv import load_dotenv
import os
import json 

load_dotenv()

client = OpenAI(
    api_key = os.environ.get('API_KEY')
)

example_json = {
  "trip_planner": {
    "Day 1": [
    {
      "name": "",
      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi eleifend lectus magna, a rhoncus erat auctor ac. Sed sodales sapien non lectus bibendum consequat. Class aptent taciti sociosqu ad fusce.",
      "coordinates" : {
          "latitude" : "00.000000",
          "longitude" : "00.000000"
      }
    },
    {
      "name": "",
      "description": "",
      "coordinates" : {
          "latitude" : "00.000000",
          "longitude" : "00.000000"
      }
    }
    
    ],
    "Day 2": [
        {
        "name": "",
        "description": "",
        "coordinates" : {
          "latitude" : "00.000000",
          "longitude" : "00.000000"
      }
    }
    ]
  }
}

def query(city, days):
  prompt = '''
  Provide valid JSON output. Provide a {days} day trip in {city} with at least 4 places to visit every day in {city}. 
  Provide one column "name", one column "description" representing the description of the possibilities to do in that visit: text with a minimum 200 characters and a maximum 250 characters, 
  and one column object "coordinates" representing the latitude and longitude.
  '''

  formatted_prompt = prompt.format(days=days, city=city)

  # specifications
  chat_completion = client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      # model="gpt-3.5-turbo",
      response_format={"type": "json_object"},
      messages=[
          {"role": "system", "content": "Provide output in valid JSON. The data schema should be like this: " + json.dumps(example_json)},
          {"role": "user", "content": formatted_prompt}
      ]
  )

  finish_reason = chat_completion.choices[0].finish_reason

  if(finish_reason == 'stop'):
      data = chat_completion.choices[0].message.content

      places = json.loads(data)
      return data
  else:
      return "Error! Provide more tokens"

# query("Santiago de Compostela", 2)