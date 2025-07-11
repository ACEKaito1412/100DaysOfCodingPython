from service import get_text_from_pdf
from gc_tts import TTService
import sys, os

if len(sys.argv) != 3:
    print("No required argument found while executing the program.")
    print("[1] file path | [2] output path")
    exit()

file_path = sys.argv[1]
output_path = sys.argv[2]


if os.path.exists(file_path):
    text = get_text_from_pdf(file_path)

    ts_service = TTService(file_path)
    ts_service.convert_text_to_speech(text_content=text, output_path=output_path)
    
else:
    print(f"Argument [1] {file_path} does not exist.")