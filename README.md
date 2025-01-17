<p align="center">
  <h1>📊 <strong>SIR Model Simülasyonu</strong></h1>
</p>


<p align="center">
  <img src="https://img.shields.io/badge/Platform-Python-orange">
  <img src="https://img.shields.io/badge/Language-Python-blue">
  <img src="https://img.shields.io/badge/Library-Streamlit-green">
</p>

### EN <img src="https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg" alt="British Flag" width="20" height="15">
This app simulates the spread of infectious diseases using the SIR (Susceptible, Infected, Recovered) model, with separate parameters for young and old populations. The simulation allows users to interactively adjust key parameters like transmission and recovery rates and visualize the results in real-time.

## 🚀 Features

• 🌍 *Interactive Visualization*: Easily visualize the disease spread in real-time for both young and old populations.  
• 🧑‍💻 *User Input*: Adjust parameters such as transmission rate, recovery rate, initial infected individuals, and total population size.  
• 📊 *Results Display*: View detailed results in tables and graphs, with explanatory comments on the dynamics of the spread.  
• ⚙️ *Customization*: Customize the parameters to simulate various pandemic scenarios and explore different outcomes.

### TR <img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Flag_of_Turkey.svg" alt="Türk Bayrağı" width="20" height="15">
Bu uygulama, bulaşıcı hastalıkların yayılmasını SIR (Susceptible, Infected, Recovered) modelini kullanarak simüle eder. Genç ve yaşlı nüfuslar için ayrı parametrelerle çalışan simülasyon, kullanıcıların virüs yayılma ve iyileşme oranlarını interaktif olarak ayarlamalarına ve sonuçları gerçek zamanlı görselleştirmelerine olanak tanır.

## 📋 Kullanım

Uygulama açıldıktan sonra, aşağıdaki parametreleri kaydırıcılar aracılığıyla ayarlayabilirsiniz:

• Beta (Genç): Gençler için virüsün yayılma oranı.
• Gamma (Genç): Gençlerin iyileşme oranı.
• Beta (Yaşlı): Yaşlılar için virüsün yayılma oranı.
• Gamma (Yaşlı): Yaşlıların iyileşme oranı.
• Gün: Görselleştirilecek günü seçin.
• Toplam Nüfus: Toplam nüfus büyüklüğü.
• Başlangıç Genç Enfekte: Başlangıçtaki enfekte gençlerin sayısı.
• Başlangıç Yaşlı Enfekte: Başlangıçtaki enfekte yaşlıların sayısı.

Simülasyon tamamlandığında, modelin çıktıları hem grafik hem de tablo olarak görselleştirilir. Aynı zamanda simülasyon sonuçları hakkında açıklamalar da sağlanır.

## 📊 Model Açıklamaları

Simülasyon sonuçları şu anahtar faktörlere dayanır:

• Genç Nüfus: Gençler, daha fazla etkileşimde bulundukları için genellikle daha hızlı bir yayılma gösterirler.
• Yaşlı Nüfus: Yaşlılar, daha kırılgan oldukları için hastalık daha hızlı yayılabilir.
• Beta (Virüs Yayılma Oranı): Bu değer, virüsün yayılma hızını belirler. Gençler ve yaşlılar için farklı beta değerleri ayarlanabilir.
• Gamma (İyileşme Oranı): Bu değer, bireylerin ne kadar hızlı iyileşeceğini belirler. Gençler için genellikle daha yüksek, yaşlılar için daha düşük olabilir.

## 🔍 Açıklamalar

• Eğer genç nüfusta daha fazla enfekte kişi gözlemleniyorsa, bu genellikle daha hızlı bir yayılma ve gençlerin daha fazla etkileşimde bulunmasından kaynaklanır.
• Eğer yaşlı nüfusta daha fazla enfekte kişi gözlemleniyorsa, bu durumda yaşlıların daha kırılgan olduğu ve hastalığın yayılmasının daha fazla olduğu düşünülmelidir.
• Beta değeri (yayılma oranı) gençler için daha yüksekse, gençler arasında daha hızlı bir yayılma beklenir. Yaşlılar için daha yüksekse, yaşlılar arasında daha hızlı bir yayılma beklenir.
• Eğer gamma (iyileşme oranı) değeri gençler için daha yüksekse, gençler daha hızlı iyileşir; yaşlılar için daha düşükse, yaşlılar daha yavaş iyileşir.
• Nüfus büyüklüğü arttıkça, hastalık daha uzun süre yayılabilir. Ancak büyük nüfuslar daha fazla doğal bağışıklığa ulaşabilirler. Küçük nüfuslarda enfeksiyon daha hızlı yayılır ve çabuk sona erer.

## 🛠️ Requirements / Gereksinimler

To run this app, you need the following Python packages:

• streamlit
• numpy
• pandas
• scipy
• matplotlib

## 🗺️ API

Streamlit
EN <img src="https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg" alt="British Flag" width="20" height="15">
This project uses Streamlit to create interactive web applications and visualizations for simulating the spread of infectious diseases.

TR <img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Flag_of_Turkey.svg" alt="Türk Bayrağı" width="20" height="15">
Bu proje, bulaşıcı hastalıkların yayılmasını simüle etmek için etkileşimli web uygulamaları ve görselleştirmeler oluşturmak için Streamlit kullanmaktadır.

## 🚀 Özellikler

• 🌍 *Etkileşimli Görselleştirme*: Genç ve yaşlı nüfuslar için hastalık yayılmasını gerçek zamanlı olarak görselleştirin.  
• 🧑‍💻 *Kullanıcı Girişi*: Yayılma oranı, iyileşme oranı, başlangıç enfekte sayısı ve toplam nüfus gibi parametreleri ayarlayın.  
• 📊 *Sonuçları Görüntüleme*: Detaylı sonuçları tablo ve grafiklerde görüntüleyin, yayılma dinamikleri hakkında açıklayıcı yorumlar alın.  
• ⚙️ *Özelleştirme*: Farklı pandemi senaryolarını simüle etmek için parametreleri özelleştirin ve farklı sonuçları keşfedin.

## 👨‍💻 Author / Yazar

• Eren Gökakın
University of Hacettepe, Department of Statistics

### EN <img src="https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg" alt="British Flag" width="20" height="15">
Follow these steps to get started by cloning the project to your local environment:
### TR <img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Flag_of_Turkey.svg" alt="Türk Bayrağı" width="20" height="15">
Projeyi kendi yerel ortamınıza klonlayarak başlamak için şu adımları izleyin:

```bash
# Clone the repository
git clone https://github.com/erengrealishh/sir-simulation.git

# Run the application using Streamlit
streamlit run sir_model_sim.py
