# DynamoDB CSV Import 가이드

## 1. CSV 파일 생성
```bash
python dynamodb_csv_generator.py
```

## 2. CSV를 DynamoDB로 Import하는 방법

### 방법 1: AWS Console 사용
1. AWS Console → DynamoDB → Tables → product
2. "Actions" → "Import from S3"
3. CSV 파일을 S3에 업로드 후 Import

## 설정 변경
`dynamodb_csv_generator.py` 파일의 `CONFIG` 딕셔너리만 수정하면 됩니다.
- `prefix`: 앞에 붙는 문자열
- `start_id`: 시작 번호
- `end_id`: 끝 번호  
- `base_price`: 기본 가격