import re
import pandas as pd
from collections import Counter
from sqlalchemy.ext.asyncio import AsyncSession
from src.api.deps import notes_list


async def analyze_notes(session: AsyncSession):
    notes = await notes_list(session)

    df = pd.DataFrame({"note": notes})
    df["word_count"] = df["note"].apply(lambda x: len(x.split()))

    total_word_count = int(df["word_count"].sum())
    avg_note_length = float(df["word_count"].mean())

    all_words = " ".join(notes).lower()
    words = re.findall(r'\b\w+\b',all_words)
    common_words = Counter(words).most_common(10)

    top_3_longest = df.nlargest(3,"word_count")["note"].tolist()
    top_3_shortest = df.nsmallest(3,"word_count")["note"].tolist()

    return {
        "total_word_count": total_word_count,
        "average_note_length": avg_note_length,
        "most_common_words": common_words,
        "top_3_longest_notes": top_3_longest,
        "top_3_shortest_notes": top_3_shortest
    }
