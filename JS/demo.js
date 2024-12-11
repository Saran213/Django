var books = []
var input = prompt('which operation you want to perform [add|delete|list|exit]')
while (input != 'exit') {
  if(input=='add'){
    addbook()
  }
  else if (input=='list') {
    listbooks()
  }
  else if (input=='delete') {
    deletebook()
  }
  else {
    console.log("Please choose valid option");
  }
  input = prompt('which operation you want to perform [add|delete|list|exit]')
}
console.log("Thanks for using our application");

function addbook(){
  var newbook = prompt('Enter book name to add')
  books.push(newbook)
}

function listbooks() {
  console.log("List of available books");
  for (book of books) {
    console.log(book);
  }
}

function deletebook() {
  var name = prompt('Enter book name to delete')
  var index = books.indexOf(name)
  if (index==-1) {
    console.log("Specified book is not available");
  }
  else {
    books.splice(index,1)
    console.log("Specified book is deleted");
  }
}
