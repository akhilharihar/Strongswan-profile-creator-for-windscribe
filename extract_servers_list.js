let selected = document.getElementById('location'),
server_list = {};

for(let x=1; x <selected.children.length; x++){
  let index = (selected[x].innerText).split(' ').map(x => x.toLowerCase()).join('_');
  server_list[index] = selected[x].value;
}

console.log(JSON.stringify(server_list));
