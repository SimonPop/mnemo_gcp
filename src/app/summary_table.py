class SummaryTable():
    hanzi: str
    pinyin: str
    translation: str

    def __init__(self, hanzi: str, pinyin: str, translation: str):
        self.hanzi = hanzi
        self.pinyin = pinyin
        self.translation = translation

    def __str__(self):
        return f"""
            <table class="styled-table">
                <thead>
                    <tr>
                        <th>Hanzi</th>
                        <th>Pinyin</th>
                        <th>Translation</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{self.hanzi}</td>
                        <td>{self.pinyin}</td>
                        <td>{self.translation}</td>
                    </tr>
                </tbody>
            </table>
        """