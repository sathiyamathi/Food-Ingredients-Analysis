# Food-Ingredients-Analysis
This project processes an uploaded image of food package ingredients using OCR to extract text. The extracted text is sent to a Gen AI model, which analyzes the ingredients and provides detailed insights, helping users better understand the food product's content.

1. Image Upload
The user is provided with an intuitive interface to upload an image of the food package, specifically focusing on the ingredients list section.

Supported formats: JPEG, PNG, etc.

The system ensures that the uploaded image meets basic quality checks (size, format) before processing.

2. Image Preprocessing
To enhance OCR performance, the uploaded image undergoes preprocessing steps such as:

Resizing to fit the OCR model's input requirements.

Grayscale conversion to remove unnecessary color noise.

Noise reduction (e.g., using Gaussian Blur) to remove distortions.

Contrast enhancement to make the text more prominent.

Thresholding or Binarization if needed, for better text visibility.

These preprocessing techniques improve the clarity and readability of the text for OCR.

3. Text Extraction (OCR)
OCR (Optical Character Recognition) is applied to extract textual data from the preprocessed image.

Libraries like Tesseract OCR (or any advanced OCR API) are used.

OCR extracts raw text, including ingredient names, commas, and sometimes other unnecessary artifacts.

4. Text Cleaning and Formatting
The raw OCR output often contains errors and inconsistencies.

Text cleaning steps include:

Removing extra whitespace, line breaks, and unwanted characters.

Correcting common OCR misreads (like "0" instead of "O").

Organizing ingredients into a clean, comma-separated list or structured format.

This step ensures the Gen AI receives clean, accurate input for better analysis.

5. Sending Text to Gen AI
The cleaned ingredients list is sent to a Gen AI model (like OpenAI's GPT, Gemini, etc.) through an API call or integrated backend service.

The prompt to the Gen AI is carefully designed, for example:

"Analyze the following food ingredients and provide insights about each ingredient, including health impacts, common uses, and any potential risks."

6. Gen AI Analysis and Insight Generation
The Gen AI model processes the ingredients and provides:

Ingredient Explanation: What each ingredient is and its typical use (e.g., emulsifier, preservative).

Health Insights: Whether the ingredient is beneficial, neutral, or harmful (e.g., artificial sweeteners, trans fats).

Overall Health Assessment: A final summary stating whether the food product seems healthy or contains concerning ingredients.

(Optional) Highlighting Red Flags: Notifying if harmful additives, high sugar, high sodium, or artificial preservatives are detected.

7. Display Insights to User
The insights generated by Gen AI are organized and displayed to the user through a clean, simple interface.


![5](https://github.com/user-attachments/assets/487daf31-7cc4-4ce9-b565-a756c51e0269)


