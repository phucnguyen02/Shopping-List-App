//Display insert input menu on button click
function showInsertInput() {
  var x = document.getElementById("inputInsertBox");
  x.style.display = (x.style.display != 'none' ? 'none' : 'block');
}


//Display edit input menu on button click
function showEditInput(obj) {
  var list_id = "inputEditBox" + findID(obj.id);
  var x = document.getElementById(list_id);
  x.style.display = (x.style.display != 'none' ? 'none' : 'block');
}

//Find the number ID portion of an ID string
function findID(str){
  var first_num = 0;
  for(let i = str.length - 1; i >= 0; i--)
    if(!isNaN(str[i]))
      first_num = i;
  return str.slice(first_num);
}

//Sends the inputted name to the server to update the database, and then updates the website
function submitInsertList(){
  var name = document.getElementById("insertList").value;
  var server_data = [{"name": name}];
  $.ajax({
    type: "POST",
    url: "/add_list",
    data: JSON.stringify(server_data),
    contentType: "application/json",
    success: function (result) {
      $("#renderLists").html((new DOMParser()).parseFromString(result, "text/html").querySelector("#renderLists").innerHTML);
    }
  });
}

//Sends the inputted name to the server to update the database, and then updates the website
function submitInsertItem(){
  const urlParams = new URLSearchParams(window.location.search);
  var id = urlParams.get("id");
  var name = document.getElementById("insertItem").value;
  var server_data = [{"name": name, "id": id}];
  $.ajax({
    type: "POST",
    url: "/add_item",
    data: JSON.stringify(server_data),
    contentType: "application/json",
    success: function (result) {
      $("#renderItems").html((new DOMParser()).parseFromString(result, "text/html").querySelector("#renderItems").innerHTML);
    }
  });
}

//Sends the inputted name and list ID to the server to update the database, and then updates the website
function editList(obj){
  var id = findID(obj.id);
  var newName = document.getElementById("editList" + id).value;
  if(!newName.trim().length)
      alert("New name cannot contain only spaces");
  else{
    var server_data = [{"id": id, "newName": newName}];
    $.ajax({
      type: "POST",
      url: "/edit_list",
      data: JSON.stringify(server_data),
      contentType: "application/json",
      success: function (result) {
        $("#renderLists").html((new DOMParser()).parseFromString(result, "text/html").querySelector("#renderLists").innerHTML);
      }
    });
  }
}

//Sends the inputted name and item ID to the server to update the database, and then updates the website
function editItem(obj){
  var item_id = findID(obj.id);
  const urlParams = new URLSearchParams(window.location.search);
  var list_id = urlParams.get("id");
  var newName = document.getElementById("editItem" + item_id).value;
  if(!newName.trim().length)
      alert("New name cannot contain only spaces");
  else{
    var server_data = [{"item_id": item_id, "list_id": list_id, "newName": newName}];
    $.ajax({
      type: "POST",
      url: "/edit_item",
      data: JSON.stringify(server_data),
      contentType: "application/json",
      success: function (result) {
        $("#renderItems").html((new DOMParser()).parseFromString(result, "text/html").querySelector("#renderItems").innerHTML);
      }
    });
  }
}

//Sends the removed list ID to the server to update the database, and then updates the website
function removeList(obj){
  var id = findID(obj.id);
  var server_data = [{"id": id}];
  $.ajax({
    type: "POST",
    url: "/remove_list",
    data: JSON.stringify(server_data),
    contentType: "application/json",
    success: function (result) {
      $("#renderLists").html((new DOMParser()).parseFromString(result, "text/html").querySelector("#renderLists").innerHTML);
    }
  });
}

//Sends the removed item ID to the server to update the database, and then updates the website
function removeItem(obj){
  var item_id = findID(obj.id);
  const urlParams = new URLSearchParams(window.location.search);
  var list_id = urlParams.get("id");
  var server_data = [{"item_id": item_id, "list_id": list_id}];
  $.ajax({
    type: "POST",
    url: "/remove_item",
    data: JSON.stringify(server_data),
    contentType: "application/json",
    success: function (result) {
      $("#renderItems").html((new DOMParser()).parseFromString(result, "text/html").querySelector("#renderItems").innerHTML);
    }
  });
}

//Makes the website only display items that contain the inputted name
function submitSearchItem(){
  var searchName = document.getElementById("searchItem").value;

  var allNames = document.querySelectorAll(".itemName");

  for(let i = 0; i<allNames.length; ++i){
    var menu_id = "menu" + findID(allNames[i].id);
    document.getElementById(menu_id).style.display = 'flex';
  }

  if(searchName)
    for(let i = 0; i<allNames.length; ++i){
      let item = allNames[i];
      if(item.innerHTML.toUpperCase().indexOf(searchName.toUpperCase()) === -1){
        var menu_id = "menu" + findID(item.id);
        document.getElementById(menu_id).style.display = 'none';
      }
    }
}