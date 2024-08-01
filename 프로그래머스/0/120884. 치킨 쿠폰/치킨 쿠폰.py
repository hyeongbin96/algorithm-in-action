def solution(chicken):
    answer = 0
    service_chicken = chicken // 10
    coupon = chicken % 10
    answer += service_chicken

    while service_chicken // 10 != 0:
        coupon += service_chicken % 10
        service_chicken = service_chicken // 10
        answer += service_chicken

    if service_chicken + coupon >= 10:
        coupon = service_chicken + coupon
        if coupon == 10:
            answer += 1
        else:
            answer += (coupon // 10) + ((coupon // 10 + coupon % 10) // 10)

    return answer