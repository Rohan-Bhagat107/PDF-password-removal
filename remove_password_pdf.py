import subprocess
import os

def unlock_pdfs_in_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            input_pdf = os.path.join(folder_path, filename)
            output_pdf = os.path.join(output_folder, filename)
            command = ["qpdf", "--decrypt", input_pdf, output_pdf]
            try:
                subprocess.run(command, check=True)
                print(f"Unlocked: {filename}")
            except subprocess.CalledProcessError:
                print(f"Failed to unlock: {filename}")
 
if __name__ == "__main__":
    while True:
        folder_path = input("Enter the folder path containing PDFs: ")
        output_folder = os.path.join(folder_path,"unlocked_pdf")
        os.makedirs(os.path.join(folder_path, "OCR_EN"))
        os.makedirs(os.path.join(folder_path, "OCR_JP"))
        if os.path.exists(output_folder):
            os.mkdir(output_folder)
        unlock_pdfs_in_folder(folder_path, output_folder)
