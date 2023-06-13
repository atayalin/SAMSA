import SentimentalAnalysis.model.model as model
import pandas as pd
import plots as plot


def predict_script(path):
    """
        @param path: file path of json file
        @return: a Pandas Dataframe of results
    """
    script = pd.read_json(path)

    results = []
    for index, row in script.iterrows():
        s, p, v = model.predict_dialogue(row["line"])
        results.append((row["speaker"], s, p, v))

    results = pd.DataFrame(results, columns=["speaker", "sentiment", "probability", "valence"])
    return results

result = predict_script("../data/raw/join.json")
plot.characters_sentiment_plot(result).show()
