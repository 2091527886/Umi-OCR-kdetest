const clients = workspace.windowList();
for (var i = 0; i < clients.length; i++) {
  print("233",clients[i].caption);
  if (clients[i].caption == "233") {
    print("yes");
    clients[i].closeWindow()
  }
}
