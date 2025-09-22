import csv
import json

# 설정값
CONFIG = {
    'prefix': 'dbdump',  # 앞에 붙는 문자열
    'start_id': 1,       # 시작값 
    'end_id': 500001,    # 끝값 
    'base_price': 1234,  # 기본 가격
    'padding_digits': 6  # 0패딩 자릿수 (예: 6이면 000001)
}

def generate_csv_for_dynamodb():
    """DynamoDB 업로드용 CSV 파일 생성"""
    filename = f"dynamodb_products_{CONFIG['prefix']}_{CONFIG['start_id']}_to_{CONFIG['end_id']}.csv"
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'name', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # 헤더 작성
        writer.writeheader()
        
        # 데이터 생성 및 작성
        for i in range(CONFIG['start_id'], CONFIG['end_id'] + 1):
            row = {
                'id': f"{CONFIG['prefix']}{i:0{CONFIG['padding_digits']}d}",
                'name': f"{CONFIG['prefix']}{i:0{CONFIG['padding_digits']}d}",
                'price': CONFIG['base_price']
            }
            writer.writerow(row)
    
    print(f"CSV 파일이 생성되었습니다: {filename}")
    print(f"총 {CONFIG['end_id'] - CONFIG['start_id'] + 1}개의 레코드가 생성되었습니다.")
    return filename

def preview_data():
    """생성될 데이터 미리보기"""
    print("생성될 데이터 미리보기:")
    print("-" * 50)
    for i in range(CONFIG['start_id'], min(CONFIG['start_id'] + 3, CONFIG['end_id'] + 1)):
        sample = {
            'id': f"{CONFIG['prefix']}{i:0{CONFIG['padding_digits']}d}",
            'name': f"{CONFIG['prefix']}{i:0{CONFIG['padding_digits']}d}",
            'price': CONFIG['base_price']
        }
        print(json.dumps(sample, indent=2))
    
    if CONFIG['end_id'] - CONFIG['start_id'] > 2:
        print("...")
        print(f"총 {CONFIG['end_id'] - CONFIG['start_id'] + 1}개 레코드")

if __name__ == "__main__":
    print("DynamoDB CSV 생성기")
    print("=" * 50)
    print(f"설정: prefix='{CONFIG['prefix']}', 범위={CONFIG['start_id']}-{CONFIG['end_id']}, 가격={CONFIG['base_price']}")
    print()
    
    preview_data()
    print()
    
    response = input("CSV 파일을 생성하시겠습니까? (y/n): ")
    if response.lower() == 'y':
        generate_csv_for_dynamodb()
    else:
        print("취소되었습니다.")
