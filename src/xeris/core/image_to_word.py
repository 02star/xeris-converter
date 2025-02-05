from PIL import Image
import pytesseract
from docx import Document


def image_to_word(img_path, output_path):

    # 识别中文（chi_sim）和英文（eng）
    text = pytesseract.image_to_string(Image.open(img_path), lang='chi_sim+eng')

    # 生成Word文档
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)


# 使用示例
image_to_word("input.jpg", "output.docx")