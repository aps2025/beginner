import openai
import requests
from typing import List, Dict, Any

class MediaAgent:
    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key

    def search_news(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        # Placeholder: Replace with real news API
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey=YOUR_NEWSAPI_KEY"
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])[:max_results]
            return [{"title": a["title"], "url": a["url"], "description": a["description"]} for a in articles]
        return []

    def summarize_article(self, text: str) -> str:
        prompt = f"Summarize the following article in 3 sentences:\n\n{text}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

    def generate_media_report(self, topic: str) -> Dict[str, Any]:
        news = self.search_news(topic)
        summaries = []
        for article in news:
            summary = self.summarize_article(article["description"] or article["title"])
            summaries.append({
                "title": article["title"],
                "url": article["url"],
                "summary": summary
            })
        report_prompt = "Create a comprehensive media report based on the following article summaries:\n"
        for s in summaries:
            report_prompt += f"- {s['title']}: {s['summary']}\n"
        report = openai.Completion.create(
            engine="text-davinci-003",
            prompt=report_prompt,
            max_tokens=300,
            temperature=0.6,
        )
        return {
            "topic": topic,
            "articles": summaries,
            "report": report.choices[0].text.strip()
        }

if __name__ == "__main__":
    # Example usage
    OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
    agent = MediaAgent(OPENAI_API_KEY)
    topic = "AI in Media"
    media_report = agent.generate_media_report(topic)
    print("Media Report on:", media_report["topic"])
    print(media_report["report"])
    for article in media_report["articles"]:
        print(f"- {article['title']} ({article['url']}): {article['summary']}")