from llama_cpp import Llama
import time
# 注意：請確保模型檔案路徑正確（相對於當前工作目錄）
llm = Llama(
    model_path="model/mistral-7b-instruct-v0.1.Q2_K.gguf",
    n_ctx=2048,      # 可依照需要與記憶體大小調整
    n_threads=4,     # 可根據你的 CPU 核心數指定
    verbose=True     # 輸出詳細推論進度（選用）
)

print("✅ 模型載入完成，開始推論...")
start = time.time()
response = llm("請簡單說明人工智慧是什麼", max_tokens=200)
end = time.time()

print("\n=== 回應內容 ===")
print(response["choices"][0]["text"])
print(f"\n⚡️ 推論時間：{end - start:.2f} 秒")
