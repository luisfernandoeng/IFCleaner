# 🏗️ **IFC Cleaner: Otimização de Arquivos IFC**

![Python](https://img.shields.io/badge/Python-3.7%20|%203.8%20|%203.9%20|%203.10-blue?logo=python) ![License](https://img.shields.io/badge/License-MIT-green) ![IFC](https://img.shields.io/badge/IFC-Cleaner-orange)

> **O IFC Cleaner é uma ferramenta Python projetada para otimizar arquivos IFC (Industry Foundation Classes), reduzindo seu tamanho ao remover elementos desnecessários, simplificar geometrias e melhorar a eficiência do modelo.**

---

## 🌟 **Recursos Principais**

✅ **Remoção de Elementos Desnecessários**:  
Remove propriedades redundantes, estilos visuais e relacionamentos não utilizados.

✅ **Simplificação de Geometria**:  
Reduz a precisão numérica e remove elementos distantes ou irrelevantes.

✅ **Compatível com Ferramentas BIM**:  
O arquivo limpo permanece funcional para instalações complementares removendo apenas elementos relacionados a arquitetura como paredes e piso.

✅ **Fácil de Usar**:  
Execute o script com apenas duas linhas de código e obtenha resultados.

---

## 🛠️ **Como Usar**

### **Pré-requisitos**

1. **Python**: Certifique-se de ter o Python instalado (versão 3.7 ou superior).  
   [Baixe aqui](https://www.python.org/downloads/).

2. **Biblioteca `ifcopenshell`**: Instale a biblioteca usando o pip:
   ```bash
   pip install ifcopenshell
   ```

### **Execução**

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/ifc-cleaner.git
   cd ifc-cleaner
   ```

2. Execute o script:
   ```python
   python clean_ifc.py "caminho/do/arquivo.ifc" "caminho/do/output.ifc"
   ```

3. Verifique o arquivo limpo no diretório especificado.

---

## 📊 **Exemplo de Resultados**

| **Métrica**               | **Antes**       | **Depois**      | **Redução** |
|---------------------------|-----------------|-----------------|-------------|
| Tamanho do Arquivo        | 423 MB          | 363 MB          | **14%**     |
| Número de Faces           | 2,056,957       | 1,028,478       | **50%**     |
| Propriedades Redundantes  | 46,072          | 0               | **100%**    |

---

## 📝 **Explicação do Código**

O script realiza as seguintes etapas:

1. **Carregamento do Modelo**:  
   Usa a biblioteca `ifcopenshell` para carregar o arquivo IFC.

2. **Remoção de Elementos Não Utilizados**:  
   Identifica e remove elementos sem representação geométrica, propriedades redundantes e estilos visuais.

3. **Simplificação de Geometria**:  
   Reduz a precisão numérica dos pontos e remove elementos distantes do centro.

4. **Salvamento do Modelo Limpo**:  
   Gera um novo arquivo IFC otimizado.

---
