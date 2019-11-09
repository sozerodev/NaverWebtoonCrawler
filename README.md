# 네이버 완결 웹툰 리스트 크롤링하기 
### [네이버 만화 페이지](https://comic.naver.com/index.nhn)에서 완결웹툰에 들어가면 보이는 [페이지](https://comic.naver.com/webtoon/finish.nhn)에서 크롤링하려고 하였으나 
   1. 제목이 7글자를 초과할 경우 끝에 `...`으로 입력되는 문제가 있었음.
   1. 위의 문제때문에 다음과 같은 [상세 페이지](https://comic.naver.com/webtoon/list.nhn?titleId=721559)에서 제목을 크롤링하려고 하였으나, 불필요한 정보(span태그)와 처리하기 힘든 공백문제(replace, split을 써도 소용이 없었음)로 인해 다른 방법을 모색
   1. 이렇게 그림은 없고 제목이 온전하게 나타나있는 [페이지](https://comic.naver.com/webtoon/finish.nhn?view=list&order=Update)에서 `제목, 별점, 작가 정보`를 크롤링함. 
   1. [상세 페이지](https://comic.naver.com/webtoon/list.nhn?titleId=721559)에서 `장르, 스토리요약 정보`를 크롤링함.
    

