import aiohttp
import time
import asyncio


[15] 응답 수신 완료: https://naver.com
[15] 텍스트 파싱 완료: https://naver.com
[24] 응답 수신 완료: https://naver.com
[9] 응답 수신 완료: https://naver.com
[0] 응답 수신 완료: https://naver.com
[24] 텍스트 파싱 완료: https://naver.com
[9] 텍스트 파싱 완료: https://naver.com

async def fetcher(session, url, index):
    print(f"[{index}] 요청 시작: {url}")
    async with session.get(url) as response:
        print(f"[{index}] 응답 수신 완료: {url}")
        text = await response.text()
        print(f"[{index}] 텍스트 파싱 완료: {url}")
        return text[:60]  # 너무 길지 않게 앞부분만 리턴


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
    print(f"총 {len(urls)}개의 요청 시작!\n")

    async with aiohttp.ClientSession() as session:
        tasks = [fetcher(session, url, idx) for idx, url in enumerate(urls)]
        result = await asyncio.gather(*tasks)

    print("\n모든 요청 완료!")
    print(f"\n샘플 결과 미리보기:\n{result[0][:50]} ...")


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"\n총 소요 시간: {end - start:.2f}초")