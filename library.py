# #Add new books and be set as available


# #Here I will need to define a variable for the input to be assigned to
 

# SET VARIABLE(directory) have the user input what type of action they would like to take(status/checkout/return/report)
# SET VARIABLE(search_criteria) and make it equal to user INPUT(user input)
# SET VARIABLE(borrower_id) and make it equal to the user INPUT(borrower id)


# SWITCH:

#     CASE: IF directory is status
#         SET VARIABLE(book_id) and make it equal to user INPUT(user input)
#         RETURN the variable for the book's status
#     CASE: ELSE IF directory is checkout OR return
#         IF book_id matches and is availalble
#             PRINT a message to the user letting them know the book is available.
#             UPDATE book_id's status to unavailable
#             SET VARIABLE(borrower_info) record data about the borrower
#             APPEND due date to variable book_id

#         ELSE IF the book_id matches and is not available
#             PRINT a message letting the user know that the book is not available until a specific date.
#         ELSE
#             PRINT a message asking the user for a valid response



