# Notes from the MIT AI in Healthcare course
-----
## The four key stages required to design an AI product:

1. Identify the behavior or "intelligence" you expect from the AI,
2. Define the business process where you will incorporate this behavior,
3. Select an AI approach/technology,
4. Develop and tinker with the software.
-----
### Stage 1. Identify the behavior or "intelligence" you expect from the AI
#### 1.1 This stage involves two key challenges: defining performance metrics and determining the scope of the AI's capabilities. It's crucial to understand how the performance frontier is evolving in your chosen domain so you can set realistic targets for the AI design. Additionally, you need to clearly define what the AI is expected to achieve, which is referred to as the scope. This stage is iterative, meaning you might revisit and refine your initial decisions after further development. 

It is important to understand the target intelligence performance metrics that we want to implement with AI as the performance frontier in our chosen domain is evolving rapidly. For example, the speed of change of the performance frontier can be seen in the recognition rate on a big dataset of images called ImageNet. The human error rate on the classification task was 5%, therefore you want to implement an AI that is as humans in this task. In just 5 years from 2010 to 2015, the recognition rate went from very bad to superhuman, this is called Superior Human Behavior. 
Business models had to forecast this evolution and take it into account into their plan. It is also important to figure out the scope of this superior behavior that we are expecting to implement. What is the intelligence we need in our application? The more precise you are with what the AI's task, the better. 

If this is the beginning of your design process, it's okay to be a bit generic and come back after
you've done a first iteration of stages two, three, and four. The second time around you may be
better equipped to address these two choices, metrics, and scope. It is also possible that the
second time around you pivot your original thinking based on finding from your first iteration,
like many self-driving companies did, lowering their standards into finding specific solutions like
detecting pedestrians or bicycles sometimes in restricted environments, like in urban
environments where many of the accidents occur.

#### 1.2 The progress and potential of Natural Language Processing (NLP)
Focuses on enabling machines to understand, interpret, and generate human language in a meaningful way. It bridges the gap between human communication and machine understanding by combining computational linguistics with machine learning and deep learning techniques.

NLP allows computers to process and analyze large amounts of natural language data, such as text or speech, to perform tasks like translation, sentiment analysis, summarization, and more. It is widely used in applications like chatbots, virtual assistants (e.g., Siri, Alexa), search engines, and automated content generation. NLP includes transformers like OpenAI's GPT-3 which was trained on all written texts available. 

It involves several steps to process and analysze language:
- **Text Preprocessing**: This includes tokenization (splitting text into words or sentences to enable world-level or subword-level analysis), removing stop words, stemming/lemmatization (reducing words to their root forms by chopping off prefixes/suffixes - useful for reducing dimensionality. Lemmatization reduces words to dictionary/basic forms or lemmas using linguistic rules), and cleaning text by removing unwanted characters. Benefits includes reduced dimensionality through vocabulary simplification, and improved model accuracy by removing noise and inconsistencies. 

  
- **Feature Extraction**: Techniques like Bag of Words, TF-IDF, and word embeddings (e.g., Word2Vec, GloVe) are used to convert text into numerical representations that machines can process, this is done by filtering out terms based on their frequency of occurance. Frequency clipping improves computational efficiency and model performance by removing high-frequency terms "stop words" that appear often but carry little semantic value, or low-frequency terms like rare words or typos that contribute little to the overall understanding of the text i.e., the Bag-of-Words model. TF-IDF is implemented using parameters like min_df (minimum document frequency - excludes terms that appear in fewer than a specified number of documents) and max_df (maximum document frequency - excludes terms that appear in more than a specified percentage of documents). These parameters control the inclusion of terms based on their frequency across the corpus. Limitations include loss of rare but important terms or domain/dataset dependency. 

  
- **Model Training**: Machine learning models are trained on preprocessed data to learn patterns and relationships. Deep learning models, such as transformers (e.g., BERT, GPT), are commonly used for advanced NLP tasks. The key steps involves data collection and pre-processing that includes a wide range of language examples i.e. accurate labels/annotations and cleaning/formating the raw text data afterwards, then choosing model architecture based on the specific NLP task such as rule-based models, statistical models and deep learning models (like transformers), afterwards training the model via training loops, adjusting its internal parameters through backpropagation to minimize errors or hyperparameter tuning such as learning rate, batch size, and number of epochs to optimize model performance. After training, evaluate the model's performance using seperate test dataset and further fine-tuning a pre-trained model on a smaller, domain-specific dataset. 


### Stage 2. Strategic and Operational Considerations
#### The first strategy is to be a best product player i.e., having the best technology possible and providing a product that incorporates all AI and all the associated features that will make it a useful products or service. The last strategy is network externalities, the focus is building the largest user base possible in a way that results in users getting more benefits as the size of the user base increases. Keep in mind that AI still struggles with deeper contextual understanding that requires real-world knowledge and cultural nuance, it also has difficulty with temporal reasoning. 
