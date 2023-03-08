# Define a method to create a group of rectangles
def create_rectangles
  # Define the coordinates of the three rectangles
  rect1 = [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]
  rect2 = [1, 0, 0], [2, 0, 0], [2, 1, 0], [1, 1, 0]
  rect3 = [2, 0, 0], [3, 0, 0], [3, 1, 0], [2, 1, 0]

  # Create a new group
  group = Sketchup.active_model.entities.add_group

  # Add the three rectangles to the group
  group.entities.add_face(rect1)
  group.entities.add_face(rect2)
  group.entities.add_face(rect3)

  # Return the group
  return group
end

# Add a menu item to run the create_rectangles method
UI.menu("Plugins").add_item("Create Rectangles") {
  create_rectangles
}
