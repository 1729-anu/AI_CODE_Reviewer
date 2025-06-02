from app.reviewer import review_code

if __name__ == "__main__":
    file_path = input("Enter path to Python code for review: ")
    review_code(file_path)
