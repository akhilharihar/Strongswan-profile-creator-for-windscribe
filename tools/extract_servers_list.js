let serverLocationOptions = document.getElementById('location'),
serverMapping = {};

for(const option of serverLocationOptions.options) {
  if(option.label == "Choose Location") continue;
  serverMapping[option.label] = option.value;
}

console.log(JSON.stringify(serverMapping));
