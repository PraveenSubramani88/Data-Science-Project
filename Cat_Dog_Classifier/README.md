## 🐶🐱 Cat vs Dog Image Classification with MobileNetV2

This project uses the pre-trained **MobileNetV2** deep learning model from TensorFlow's Keras library to classify images as either **cat**, **dog**, or **uncertain** based on their content. It leverages the **ImageNet** weights to identify the object in an image with high confidence and classify it accordingly.

---

### 📁 Project Structure

```
Cat_Dog_Classifier/
│
├── classify.py               # Main Python script
├── README.md                 # This file
├── Cat_Dog/                  # Folder containing cat and dog images
│   ├── c1.jpg
│   ├── d1.jpg
│   └── ...
```

---

### 🚀 How It Works

1. **Model**: Uses `MobileNetV2` pre-trained on ImageNet (1000-class classification).
2. **Preprocessing**: Images are resized to 224x224 and preprocessed using `preprocess_input`.
3. **Prediction**: The model returns the top predicted class.
4. **Classification Logic**:

   * If the predicted label contains `"cat"`, it's labeled as **Cat**
   * If it contains `"dog"`, it's labeled as **Dog**
   * Otherwise, it's labeled as **Uncertain**
5. **Output**: A table is printed showing the filename, classification, and raw decoded label with confidence.

---

### ✅ Requirements

Install the required Python libraries (you can use a virtual environment):

```bash
pip install tensorflow numpy
```

---

### 🧠 What I Learned

1. **Image Classification with Pre-trained Models**
   I learned how to use TensorFlow's `MobileNetV2` to classify images without needing to train a model from scratch.

2. **Preprocessing for CNNs**
   I understood the importance of resizing and normalizing input images using `preprocess_input` to match the model's expectations.

3. **Decoding Predictions**
   I learned how to use `decode_predictions` to convert raw output probabilities into human-readable labels and interpret top-k predictions.

4. **Confidence Scores**
   I understood how to interpret the confidence values (`decoded[0][2]`) and use them to make more informed classification decisions.

5. **Automation with File Handling**
   I practiced automating batch prediction tasks by reading files from a directory and applying classification in a loop.

6. **Output Formatting**
   I gained experience in printing structured console output using Python’s string formatting tools.

---

### 🖼️ Sample Output

```
Filename                       Prediction              
-----------------------------------------------
d1.jpg                       Dog             
c2.png                       Cat             
d5.jpg                       Uncertain (Labrador) 
```

---

### 🔍 Notes

* The model uses **ImageNet** labels. It recognizes specific breeds like `Siamese_cat`, `Persian_cat`, `golden_retriever`, `Labrador`, etc.
* It might classify unusual images (e.g., raccoons, foxes) as **Uncertain** since they don't contain the keywords `"cat"` or `"dog"`.

---

### 📌 Future Improvements

* Add a **confidence threshold** (e.g., only classify if confidence > 0.7).
* Save the output to a **CSV file**.
* Visualize predictions using matplotlib.
* Fine-tune the model on a custom cat/dog dataset for improved accuracy.
