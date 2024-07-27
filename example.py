from openai import OpenAI
import json

f = open("api_key.txt", "r");

client = OpenAI(
    api_key = f.read()
)

example_json = {
  "ski_resorts": [
    {
      "name": "Les 3 Vallées",
      "slope_kilometers": 600
    },
  ]
}

prompt = "Provide valid JSON output. Provide the top 10 largest ski resorts in Europe. Rankikng them on slope kilometers (descending) Provide one column 'name' and a column 'slope_column' representing the total slope kilometers"

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={"type": "json_object"},
    # max_tokens=
    messages=[
        {"role": "system", "content": "Provide output in valid JSON. The data schema should be like this: " + json.dumps(example_json)},
        {"role": "user", "content": prompt}
    ]
)

finish_reason = chat_completion.choices[0].finish_reason

if(finish_reason == 'stop'):
    data = chat_completion.choices[0].message.content

    ski_resorts = json.loads(data)

    for ski_r in ski_resorts['ski_resorts']:
        print(ski_r['name'] + " : " + str(ski_r['slope_kilometers']) + "km")
else:
    print("Error! Provide more tokens")


# print(json.dumps(example_json))