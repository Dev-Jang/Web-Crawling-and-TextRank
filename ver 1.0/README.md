# Web-Crawling-and-TextRank (Ver 1.0)

Boilerpipe3 와 TextRank 모듈을 동시에 사용할 수 없어서 실패.

각각의 파일로는 실행가능.

<br>
<br>

## Crawling.py

<br>

<b>Function</b>
- To crawl only Naver blog posts through Naver search

<br>

<b>Process</b>
- 검색단어 입력
- 검색건수 출력
- 검색번호 입력
- 제목과 내용 출력

<pre><code><b>Execution result</b>

> 검색단어 : [입력]
검색된 결과 <건수> 건
> 검색번호(1-1000) : [입력]
- 제목 : <포스트 제목>
- 내용
<포스트 내용(텍스트)>
</code></pre>

<br>
<br>

## TextRank.py

<br>

<b>Function</b>
- Summarize documents using the TextRank algorithm
- Output key words by weighting each word

<br>

<b>Process</b>
- Crawl Text
- Sentence division
- Natural language processing(NLP)
- TF-IDF Model
- Generate graph
- Apply TextRank

<pre><code><b>Execution result</b>

<요약>
keywords : <키워드 리스트>
</code></pre>

<br>
<br>

## Reference
https://excelsior-cjh.tistory.com/93
