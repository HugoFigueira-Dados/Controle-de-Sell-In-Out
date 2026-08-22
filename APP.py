# CONFIGURAÇÃO DA PÁGINA STREAMLIT
# ________________________________
st.set_page_config(
    page_title="XZ Variedades - Gestão & Estoque",
    page_icon="🛍️",
    page_title="Controle de Sell-In/Out | Gestão & Estoque",
    page_icon="📦",
layout="wide"
)

# Bloco 1: Leitura do estoque e tipos de dados
def limpar_nome_produto(nome):

def carregar_estoque():
if os.path.exists(ARQUIVO_ESTOQUE):
        df = pd.read_csv(ARQUIVO_ESTOQUE)
        df = pd.read_csv(ARQUIVO_ESTOQUE, dtype={'sku': str, 'ultimo_pedido_id': str})
if 'margem_porcentagem' not in df.columns:
df['margem_porcentagem'] = 0.0
return df

# Bloco 2: Leitura de vendas e tratamento de IDs
def carregar_vendas():
if os.path.exists(ARQUIVO_VENDAS):
        return pd.read_csv(ARQUIVO_VENDAS)
        return pd.read_csv(ARQUIVO_VENDAS, dtype={'sku': str, 'id_venda': str})
else:
return pd.DataFrame(columns=[
'id_venda', 'sku', 'nome_produto', 'quantidade_vendida', 

# Bloco 3: Tratamento de exceções no CSV
def processar_csv_upload(uploaded_file, df_estoque):
if len(df_novo.columns) < 2:
uploaded_file.seek(0)
df_novo = pd.read_csv(uploaded_file, sep=';')
        except:
        except Exception:
uploaded_file.seek(0)
df_novo = pd.read_csv(uploaded_file, sep=';')

# Bloco 4: Título da barra lateral
# ________________________________
# INTERFACE GRÁFICA (SIDEBAR E NAVEGAÇÃO)
# ________________________________
st.sidebar.title("🛍️ XZ Variedades")
st.sidebar.title("📦 Gestão de Vendas & PDV")
st.sidebar.markdown("---")

menu = st.sidebar.radio(

# Bloco 5: Remoção da limpeza de df_edit ao zerar dados
])

salvar_dados(df_estoque_zerado, df_vendas_zerado)
    if "df_edit" in st.session_state:
        del st.session_state["df_edit"]
st.sidebar.success("Todos os dados foram zerados!")
st.rerun()

# Bloco 6: Métricas da Dashboard
col4.metric("Prev. Lucro Total (Estoque)", f"R$ {prev_lucro:.2f}")

col_m1, col_m2 = st.columns(2)
    col_m1.metric("📈 % Margem de Lucro Real (Até o momento)", f"{margem_real_pct:.2f}%")
    col_m2.metric("📦 % Margem de Lucro Total (Estoque Projetado)", f"{margem_estoque_pct:.2f}%")
    col_m1.metric("📈 % Margem de Lucro Real", f"{margem_real_pct:.2f}%")
    col_m2.metric("📦 % Margem de Lucro Projetada", f"{margem_estoque_pct:.2f}%")

st.markdown("---")
st.subheader("📋 Histórico Recente de Vendas")

# Bloco 7: Simplificação da edição da tabela de estoque
st.info("Nenhuma venda registrada até o momento.")

# ________________________________
# ABA 2: ESTOQUE E PREÇOS (RECALCULANDO MARGEM AO DIGITAR)
# ABA 2: ESTOQUE E PREÇOS
# ________________________________
elif menu == "📦 Estoque & Preços":
st.title("📦 Gerenciamento de Estoque e Margens")

if not df_estoque.empty:
        st.caption("💡 Digite um novo valor em **Preço de Venda (R$)** e aperte **Enter**. A **% Margem Lucro** será recalculada automaticamente!")
        st.caption("💡 Edite os valores na tabela e clique no botão **Salvar Alterações nos Preços** para confirmar.")

        # Atualiza a cópia no session_state para manter sincronizado com o estoque atualizado
        st.session_state.df_edit = df_estoque.copy()

        # Recalcular margem para cada linha exibida na tela
        st.session_state.df_edit['margem_porcentagem'] = st.session_state.df_edit.apply(
        df_display = df_estoque.copy()
        df_display['margem_porcentagem'] = df_display.apply(
lambda row: round(((row['preco_venda_unitario'] - row['custo_total_unitario']) / row['custo_total_unitario']) * 100, 2)
if row['custo_total_unitario'] > 0 else 0.0, axis=1
)

        # Tabela editável
edited_df = st.data_editor(
            st.session_state.df_edit,
            df_display,
column_config={
"sku": st.column_config.TextColumn("SKU", disabled=True),
"nome_produto": st.column_config.TextColumn("Produto", disabled=True),

# Bloco 8: Remoção da reavaliação em tempo real e salvamento manual
key="tabela_editor_interativo"
)

        # Se houver modificações na tabela, atualiza o estado e recarrega
        if not edited_df.equals(st.session_state.df_edit):
            salvar_dados(edited_df, df_vendas)
            st.session_state.df_edit = edited_df
            st.rerun()

if st.button("💾 Salvar Alterações nos Preços", use_container_width=True):
            salvar_dados(st.session_state.df_edit, df_vendas)
            salvar_dados(edited_df, df_vendas)
st.toast("Preços e margens salvos com sucesso!", icon="✅")
st.rerun()
else:

# Bloco 9: Registro de Vendas
df_vendas = pd.concat([df_vendas, pd.DataFrame([nova_venda])], ignore_index=True)

salvar_dados(df_estoque, df_vendas)
                if "df_edit" in st.session_state:
                    del st.session_state["df_edit"]
st.toast(f"Venda de {qtd_venda}x '{item['nome_produto']}' registrada!", icon="🎉")
st.rerun()
else:

# Bloco 10: Processamento de Pedido
if arquivo_upload is not None:
if st.button("🚀 Processar Pedido", use_container_width=True):
            with st.spinner("Processando itens, calculando frete e gerando preços sugeridos (150% de lucro)..."):
            with st.spinner("Processando itens e calculando rateio de frete..."):
df_estoque, sucesso, qtd_itens, frete = processar_csv_upload(arquivo_upload, df_estoque)

if sucesso:
salvar_dados(df_estoque, df_vendas)
                if "df_edit" in st.session_state:
                    del st.session_state["df_edit"]
st.success("✅ Pedido processado e adicionado ao estoque!")
st.toast("Estoque atualizado com sucesso!", icon="📦")
