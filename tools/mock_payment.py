def tool_mock_payment(amount):
    print(f"💵 Processing payment of ${amount}...")
    # Simulate delay
    import time; time.sleep(1)
    print("✅ Payment successful!")
    return True
