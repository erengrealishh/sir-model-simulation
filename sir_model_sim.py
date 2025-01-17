import streamlit as st
import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# SIR modelinin diferansiyel denklemleri (iki grup: Genç ve Yaşlı)
def sir_model_with_risk_groups(y, t, beta_young, gamma_young, beta_old, gamma_old, N):
    S_young, I_young, R_young, S_old, I_old, R_old = y
    # Gençler için denklemler
    dS_young_dt = -beta_young * S_young * I_young / N
    dI_young_dt = beta_young * S_young * I_young / N - gamma_young * I_young
    dR_young_dt = gamma_young * I_young

    # Yaşlılar için denklemler
    dS_old_dt = -beta_old * S_old * I_old / N
    dI_old_dt = beta_old * S_old * I_old / N - gamma_old * I_old
    dR_old_dt = gamma_old * I_old

    return [dS_young_dt, dI_young_dt, dR_young_dt, dS_old_dt, dI_old_dt, dR_old_dt]

# Başlangıç parametreleri (İlk Nüfus ve Enfekte Sayısı)
def run_simulation(beta_young, gamma_young, beta_old, gamma_old, day, N, I0_young, I0_old):
    # Başlangıç değerleri (Gençler ve Yaşlılar için)
    S0_young = 0.8 * N - I0_young
    S0_old = 0.2 * N - I0_old
    y0 = [S0_young, I0_young, 0, S0_old, I0_old, 0]  # Başlangıçta iyileşenler sıfır

    # ODE çözümü
    t = np.linspace(0, 100, 101)
    solution = odeint(sir_model_with_risk_groups, y0, t, args=(beta_young, gamma_young, beta_old, gamma_old, N))
    S_young, I_young, R_young, S_old, I_old, R_old = solution.T
    
    # Seçilen günün verilerini almak
    idx = int(day)  # Günü seçmek için index
    data = {
        'Grup': ['Genç Duyarlı (S)', 'Genç Enfekte (I)', 'Genç İyileşen (R)', 
                 'Yaşlı Duyarlı (S)', 'Yaşlı Enfekte (I)', 'Yaşlı İyileşen (R)'],
        'Nüfus Sayısı': [round(S_young[idx]), round(I_young[idx]), round(R_young[idx]), 
                         round(S_old[idx]), round(I_old[idx]), round(R_old[idx])]
    }
    df = pd.DataFrame(data)
    
    # Sonuçları görselleştirme: sadece seçilen güne kadar olanları çiziyoruz
    plt.figure(figsize=(10, 6))
    plt.plot(t[:idx+1], S_young[:idx+1], label='Genç Duyarlı (S)')
    plt.plot(t[:idx+1], I_young[:idx+1], label='Genç Enfekte (I)')
    plt.plot(t[:idx+1], R_young[:idx+1], label='Genç İyileşen (R)')
    plt.plot(t[:idx+1], S_old[:idx+1], label='Yaşlı Duyarlı (S)', linestyle='--')
    plt.plot(t[:idx+1], I_old[:idx+1], label='Yaşlı Enfekte (I)', linestyle='--')
    plt.plot(t[:idx+1], R_old[:idx+1], label='Yaşlı İyileşen (R)', linestyle='--')
    
    plt.title(f'SIR Modeli: Gün {day} Sonuçları - Beta ve Gamma Değerleri ({beta_young}, {gamma_young}, {beta_old}, {gamma_old})')
    plt.xlabel('Zaman (gün)')
    plt.ylabel('Nüfus Sayısı')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    
    # Tabloyu yazdır
    st.write(f"Sonuçlar (Gün {day}):")
    st.write(df)
    
    # Açıklamalar
    st.write("\n### Model Sonuçlarıyla İlgili Açıklamalar:")
    if I_young[idx] > I_old[idx]:
        st.write("- Genç nüfusta daha fazla enfekte kişi gözlemleniyor, bu genellikle daha hızlı bir yayılma ve gençlerin daha fazla etkileşimde bulunmasından kaynaklanır.")
    else:
        st.write("- Yaşlı nüfusta daha fazla enfekte kişi gözlemleniyor, bu durumda yaşlıların daha kırılgan olduğu ve hastalığın yayılmasının daha fazla olduğu düşünülmelidir.")
    
    if beta_young > beta_old:
        st.write("- Gençler arasında daha hızlı bir yayılma bekleniyor, çünkü beta değeri (virüsün yayılma oranı) gençler için daha yüksek.")
    else:
        st.write("- Yaşlılar arasında daha hızlı bir yayılma bekleniyor, çünkü beta değeri yaşlılar için daha yüksek.")
    
    if gamma_young < gamma_old:
        st.write("- Gençler daha hızlı iyileşiyor, çünkü gamma değeri (iyileşme oranı) gençler için daha yüksek.")
    else:
        st.write("- Yaşlılar daha yavaş iyileşiyor, çünkü gamma değeri yaşlılar için daha düşük.")
    
    if N > 2000:
        st.write("- Nüfusun büyüklüğü arttıkça, hastalık daha uzun süre yayılabilir. Ancak büyük nüfuslar daha fazla doğal bağışıklığa ulaşabilirler.")
    else:
        st.write("- Küçük nüfuslarda, enfeksiyon daha hızlı bir şekilde yayılabilir ve daha çabuk sona erer.")

# Kullanıcıdan etkileşimli giriş almak için kaydırıcılar
st.title("SIR Modeli Uygulaması")

beta_young = st.slider('Beta (Genç)', 0.0, 1.0, 0.2)
gamma_young = st.slider('Gamma (Genç)', 0.0, 1.0, 0.1)
beta_old = st.slider('Beta (Yaşlı)', 0.0, 1.0, 0.4)
gamma_old = st.slider('Gamma (Yaşlı)', 0.0, 1.0, 0.05)
day = st.slider('Gün', 0, 100, 100)
N = st.slider('Toplam Nüfus', 500, 5000, 1000)
I0_young = st.slider('Başlangıç Genç Enfekte', 0, 100, 1)
I0_old = st.slider('Başlangıç Yaşlı Enfekte', 0, 100, 1)

# Simülasyonu çalıştır ve sonuçları göster
run_simulation(beta_young, gamma_young, beta_old, gamma_old, day, N, I0_young, I0_old)
