function removeElement(e, id) {
  let button = e.target;

  let div = button.parentElement;
  let field = button.previousElementSibling;
  let search_by_text = field.previousElementSibling;
  let label = search_by_text.previousElementSibling
  let br = button.nextElementSibling;
  
  div.removeChild(button);
  div.removeChild(field);
  div.removeChild(search_by_text);
  div.removeChild(label);
  div.removeChild(br);

  let allElements = document.getElementById(id);
  let inputs = allElements.getElementsByTagName("input");
  let input_id = allElements.getElementsByTagName("input").length;

  for(i = input_id; i < inputs.length; i++){
    inputs[i].setAttribute('id', (i + 1));
    inputs[i].setAttribute('value', (i + 1));
    inputs[i].nextSibling.setAttribute('id', (i + 1));
  }
}

function add(key, id) {
  console.log(key, id)
  let allElements = document.getElementById(key);
  let input_id = allElements.getElementsByTagName("input").length;

  input_id++;

  //create label tag
  let label = document.createElement('label');
  label.htmlFor = input_id
  label.innerHTML = " + "
  label.style.marginLeft = "75px"

  //create input tag
  let input = document.createElement('input');
  input.type = "text";
  // input.setAttribute("class", "w3-input w3-border");
  input.setAttribute('id', input_id);
  input.setAttribute('type', "text")
  input.setAttribute('value', "");
  input.setAttribute('name', key);
  input.setAttribute('class', "submitform")
  
  let reqs = document.getElementById(key);

  //create remove button
  let remove = document.createElement('button');
  remove.setAttribute('id', input_id);
  // remove.setAttribute('type', "button");
  remove.setAttribute('class', 'fas fa-minus-square')
  remove.setAttribute('name', "removebtn");
  // remove.innerHTML = "Remove";
  remove.style.marginLeft = "5px";
  remove.onclick = function(e) {
    removeElement(e, id);
  };

  let search_by_text = document.createElement('button');
  search_by_text.setAttribute('id', input_id);
  search_by_text.setAttribute('class', 'fas fa-search')
  search_by_text.setAttribute('name', 'search_by_text');
  search_by_text.setAttribute('type', 'submit')

  let br = document.createElement("br");

  //append elements
  reqs.appendChild(label)
  reqs.appendChild(input)
  reqs.appendChild(search_by_text)
  reqs.appendChild(remove);
  reqs.appendChild(br);
  // reqs.appendChild(add_btn)
}