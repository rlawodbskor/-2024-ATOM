def calculate_energy(weight, length, time):
    gravity = 9.81  # 중력 가속도 (m/s^2)

    # 높이 변화 계산: v = gt, h = 0.5 * g * t^2
    height = 0.5 * gravity * time**2

    # 에너지 변화 계산: E = mgh + 0.5 * m * v^2
    potential_energy = weight * gravity * height
    kinetic_energy = 0.5 * weight * (length / time)**2

    total_energy = potential_energy + kinetic_energy

    return total_energy

def main():
    # 사용자 입력 받기
    weight = float(input("롤러코스터의 차체 무게를 입력하세요 (kg): "))
    length = float(input("레일 노선의 길이를 입력하세요 (m): "))
    time = float(input("롤러코스터의 완주 시간을 입력하세요 (s): "))

    # 역학적 에너지 계산
    energy = calculate_energy(weight, length, time)
    print("롤러코스터의 역학적 에너지는 {:.2f} 제곱미터/초^2 입니다.".format(energy))

if __name__ == "__main__":
    main()
