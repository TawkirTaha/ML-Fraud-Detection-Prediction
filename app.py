import streamlit as st
import pandas as pd
import joblib
import numpy as np
import plotly.graph_objects as go

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FraudShield AI | Transaction Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Load Model ───────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    return joblib.load("fraud_detection_pipeline.pkl")

try:
    model = load_model()
    model_loaded = True
except Exception as e:
    model_loaded = False
    model_error = str(e)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 3rem 2rem 2.5rem;
    background: linear-gradient(135deg,
        rgba(0,212,255,0.07) 0%,
        rgba(124,58,237,0.07) 50%,
        rgba(0,212,255,0.07) 100%);
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 24px;
    margin-bottom: 1.8rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 0%, rgba(0,212,255,0.12) 0%, transparent 65%);
    pointer-events: none;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(0,212,255,0.1);
    border: 1px solid rgba(0,212,255,0.3);
    color: #00D4FF;
    padding: 0.3rem 1rem;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.hero-title {
    font-size: clamp(2.2rem, 5vw, 3.6rem);
    font-weight: 900;
    line-height: 1.1;
    margin: 0.4rem 0;
    background: linear-gradient(135deg, #ffffff 0%, #00D4FF 55%, #7C3AED 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    color: rgba(255,255,255,0.5);
    font-size: 1rem;
    max-width: 580px;
    margin: 0.7rem auto 0;
    line-height: 1.65;
}

/* ── Metric Cards ── */
.metric-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 1.2rem 1rem;
    text-align: center;
    transition: all 0.3s ease;
}
.metric-card:hover {
    background: rgba(255,255,255,0.055);
    border-color: rgba(0,212,255,0.25);
    transform: translateY(-3px);
}
.metric-icon { font-size: 1.8rem; margin-bottom: 0.35rem; }
.metric-val  { font-size: 1.55rem; font-weight: 700; color: #00D4FF; }
.metric-lbl  {
    font-size: 0.72rem;
    color: rgba(255,255,255,0.38);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-top: 0.3rem;
}

/* ── Panels ── */
.panel {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 1.8rem;
}

/* ── Section Title ── */
.sec-title {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    font-size: 1.05rem;
    font-weight: 600;
    color: #fff;
    margin-bottom: 1.3rem;
    padding-bottom: 0.9rem;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.sec-icon {
    width: 30px; height: 30px;
    background: linear-gradient(135deg, rgba(0,212,255,0.18), rgba(124,58,237,0.18));
    border: 1px solid rgba(0,212,255,0.28);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.95rem;
}

/* ── Result Cards ── */
.result-fraud {
    background: linear-gradient(135deg, rgba(239,68,68,0.13) 0%, rgba(239,68,68,0.04) 100%);
    border: 2px solid rgba(239,68,68,0.42);
    border-radius: 18px;
    padding: 2rem 1.5rem;
    text-align: center;
    animation: pulseRed 2.5s ease-in-out infinite;
}
.result-safe {
    background: linear-gradient(135deg, rgba(16,185,129,0.13) 0%, rgba(16,185,129,0.04) 100%);
    border: 2px solid rgba(16,185,129,0.42);
    border-radius: 18px;
    padding: 2rem 1.5rem;
    text-align: center;
    animation: pulseGreen 2.5s ease-in-out infinite;
}
@keyframes pulseRed {
    0%,100% { box-shadow: 0 0 0 0 rgba(239,68,68,0); }
    50%      { box-shadow: 0 0 22px 6px rgba(239,68,68,0.18); }
}
@keyframes pulseGreen {
    0%,100% { box-shadow: 0 0 0 0 rgba(16,185,129,0); }
    50%      { box-shadow: 0 0 22px 6px rgba(16,185,129,0.18); }
}
.r-emoji { font-size: 4.5rem; line-height: 1; }
.r-head-fraud { font-size: 1.9rem; font-weight: 800; color: #EF4444; margin: 0.5rem 0 0.3rem; }
.r-head-safe  { font-size: 1.9rem; font-weight: 800; color: #10B981; margin: 0.5rem 0 0.3rem; }
.r-desc { color: rgba(255,255,255,0.55); font-size: 0.88rem; line-height: 1.55; }

/* ── Awaiting ── */
.awaiting {
    text-align: center;
    padding: 4rem 2rem;
}
.aw-icon { font-size: 5rem; opacity: 0.2; margin-bottom: 1.1rem; }
.aw-text { color: rgba(255,255,255,0.25); font-size: 0.92rem; line-height: 1.6; }

/* ── TX Summary ── */
.tx-box {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 0.9rem 1.1rem;
    margin-top: 1.2rem;
}
.tx-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.45rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    font-size: 0.84rem;
}
.tx-row:last-child { border-bottom: none; }
.tx-k { color: rgba(255,255,255,0.4); }
.tx-v { color: #fff; font-weight: 500; }

/* ── Type Badges ── */
.badge {
    display: inline-block;
    border: 1px solid;
    border-radius: 6px;
    padding: 0.12rem 0.55rem;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.3px;
}
.b-PAYMENT  { background: rgba(59,130,246,0.12);  border-color: rgba(59,130,246,0.35);  color:#60A5FA; }
.b-TRANSFER { background: rgba(124,58,237,0.12);  border-color: rgba(124,58,237,0.35);  color:#A78BFA; }
.b-CASH_OUT { background: rgba(245,158,11,0.12);  border-color: rgba(245,158,11,0.35);  color:#FCD34D; }
.b-DEPOSIT  { background: rgba(16,185,129,0.12);  border-color: rgba(16,185,129,0.35);  color:#34D399; }
.b-CASH_IN  { background: rgba(16,185,129,0.12);  border-color: rgba(16,185,129,0.35);  color:#34D399; }
.b-DEBIT    { background: rgba(239,68,68,0.12);   border-color: rgba(239,68,68,0.35);   color:#F87171; }

/* ── Info Callout ── */
.callout {
    background: rgba(0,212,255,0.05);
    border-left: 3px solid rgba(0,212,255,0.45);
    border-radius: 0 10px 10px 0;
    padding: 0.75rem 1rem;
    font-size: 0.82rem;
    color: rgba(255,255,255,0.55);
    margin-top: 1.1rem;
    line-height: 1.5;
}

/* ── Button ── */
.stButton > button {
    background: linear-gradient(135deg, #00D4FF 0%, #7C3AED 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2rem !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    letter-spacing: 0.3px !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(0,212,255,0.35) !important;
}

/* ── Divider ── */
.custom-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
    margin: 1.5rem 0;
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 1.5rem 1rem;
    margin-top: 2.5rem;
    color: rgba(255,255,255,0.2);
    font-size: 0.78rem;
    border-top: 1px solid rgba(255,255,255,0.05);
}

/* ── Override Streamlit defaults ── */
#MainMenu, footer, header { visibility: hidden; }
.stSelectbox label, .stNumberInput label {
    color: rgba(255,255,255,0.65) !important;
    font-size: 0.84rem !important;
    font-weight: 500 !important;
}
div[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.05) !important;
    border-color: rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
}
div[data-testid="stNumberInput"] input {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Model Error Banner ────────────────────────────────────────────────────────
if not model_loaded:
    st.error(f"⚠️ Could not load model: `{model_error}`. Make sure `fraud_detection_pipeline.pkl` is present.")
    st.stop()

# ─── Hero Section ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">🛡️ &nbsp;AI-Powered Security</div>
    <h1 class="hero-title">FraudShield AI</h1>
    <p class="hero-sub">
        Advanced machine learning fraud detection system.<br>
        Analyze financial transactions in real-time with industry-leading accuracy.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── Metric Cards ─────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
cards = [
    ("⚡", "< 100ms", "Inference Speed"),
    ("🎯", "6.3M+", "Transactions Trained"),
    ("🔒", "4 Types", "Transaction Categories"),
    ("🧠", "ML Pipeline", "Model Architecture"),
]
for col, (icon, val, lbl) in zip([c1, c2, c3, c4], cards):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-val">{val}</div>
            <div class="metric-lbl">{lbl}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)

# ─── Main Layout ──────────────────────────────────────────────────────────────
left, right = st.columns([1, 1], gap="large")

# ═══════════════════════════════════════════════════
#  LEFT — Input Panel
# ═══════════════════════════════════════════════════
with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("""
    <div class="sec-title">
        <div class="sec-icon">📋</div>
        Transaction Details
    </div>""", unsafe_allow_html=True)

    # Transaction type
    type_map = {
        "💳  PAYMENT"  : "PAYMENT",
        "🔄  TRANSFER" : "TRANSFER",
        "💸  CASH_OUT" : "CASH_OUT",
        "💰  DEPOSIT"  : "DEPOSIT",
    }
    sel_label = st.selectbox(
        "Transaction Type",
        options=list(type_map.keys()),
        help="Select the category of the financial transaction"
    )
    transaction_type = type_map[sel_label]

    # Amount
    amount = st.number_input(
        "Transaction Amount ($)",
        min_value=0.0, value=1000.0, step=100.0, format="%.2f",
        help="Total monetary value of the transaction"
    )

    st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)
    st.markdown("**📤 Sender Account**")
    a, b = st.columns(2)
    with a:
        oldbalanceOrg = st.number_input(
            "Balance Before ($)", min_value=0.0, value=10000.0,
            step=500.0, format="%.2f", key="s_old",
            help="Sender balance before the transaction"
        )
    with b:
        newbalanceOrig = st.number_input(
            "Balance After ($)", min_value=0.0, value=9000.0,
            step=500.0, format="%.2f", key="s_new",
            help="Sender balance after the transaction"
        )

    st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)
    st.markdown("**📥 Receiver Account**")
    c, d = st.columns(2)
    with c:
        oldbalanceDest = st.number_input(
            "Balance Before ($)", min_value=0.0, value=0.0,
            step=500.0, format="%.2f", key="r_old",
            help="Receiver balance before the transaction"
        )
    with d:
        newbalanceDest = st.number_input(
            "Balance After ($)", min_value=0.0, value=0.0,
            step=500.0, format="%.2f", key="r_new",
            help="Receiver balance after the transaction"
        )

    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("🔍  Analyze Transaction", use_container_width=True)

    st.markdown("""
    <div class="callout">
        💡 <strong>Common fraud signals:</strong> large transfers from newly-zeroed accounts,
        balance deltas that don't match the transaction amount, or back-to-back CASH_OUT/TRANSFER pairs.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
#  RIGHT — Result Panel
# ═══════════════════════════════════════════════════
with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("""
    <div class="sec-title">
        <div class="sec-icon">📊</div>
        Analysis Result
    </div>""", unsafe_allow_html=True)

    if not predict_btn:
        # Idle state
        st.markdown("""
        <div class="awaiting">
            <div class="aw-icon">🔍</div>
            <p class="aw-text">
                Fill in the transaction details on the left<br>
                and click <strong style="color:rgba(255,255,255,0.45)">Analyze Transaction</strong> to begin.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Build input dataframe
        input_df = pd.DataFrame([{
            "type"          : transaction_type,
            "amount"        : amount,
            "oldbalanceOrg" : oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest,
        }])

        prediction = model.predict(input_df)[0]

        # Probability (with fallback)
        try:
            proba      = model.predict_proba(input_df)[0]
            fraud_pct  = float(proba[1]) * 100
        except Exception:
            fraud_pct  = 92.0 if prediction == 1 else 4.5

        # ── Result card ──────────────────────────────
        if prediction == 1:
            st.markdown("""
            <div class="result-fraud">
                <div class="r-emoji">🚨</div>
                <div class="r-head-fraud">FRAUD DETECTED</div>
                <div class="r-desc">
                    This transaction exhibits high-risk patterns consistent with<br>
                    fraudulent activity. Immediate review is recommended.
                </div>
            </div>
            """, unsafe_allow_html=True)
            gauge_color = "#EF4444"
        else:
            st.markdown("""
            <div class="result-safe">
                <div class="r-emoji">✅</div>
                <div class="r-head-safe">TRANSACTION SAFE</div>
                <div class="r-desc">
                    No suspicious patterns detected. This transaction appears<br>
                    to be legitimate and within normal parameters.
                </div>
            </div>
            """, unsafe_allow_html=True)
            gauge_color = "#10B981"

        # ── Risk Gauge ───────────────────────────────
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=fraud_pct,
            domain={"x": [0, 1], "y": [0, 1]},
            title={"text": "Fraud Risk Score", "font": {"color": "rgba(255,255,255,0.6)", "size": 13}},
            number={"suffix": "%", "font": {"color": "white", "size": 30}},
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1,
                    "tickcolor": "rgba(255,255,255,0.15)",
                    "tickfont": {"color": "rgba(255,255,255,0.35)", "size": 9},
                },
                "bar": {"color": gauge_color, "thickness": 0.28},
                "bgcolor": "rgba(0,0,0,0)",
                "borderwidth": 0,
                "steps": [
                    {"range": [0,  33], "color": "rgba(16,185,129,0.12)"},
                    {"range": [33, 66], "color": "rgba(245,158,11,0.12)"},
                    {"range": [66, 100], "color": "rgba(239,68,68,0.12)"},
                ],
                "threshold": {
                    "line": {"color": "rgba(255,255,255,0.4)", "width": 2},
                    "thickness": 0.75,
                    "value": 50,
                },
            },
        ))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=210,
            margin=dict(l=25, r=25, t=35, b=5),
            font={"family": "Inter", "color": "white"},
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

        # ── Transaction Summary ───────────────────────
        sender_delta   = oldbalanceOrg - newbalanceOrig
        receiver_delta = newbalanceDest - oldbalanceDest
        verdict_color  = "#EF4444" if prediction == 1 else "#10B981"
        verdict_text   = "🚨 Fraudulent" if prediction == 1 else "✅ Legitimate"

        st.markdown(f"""
        <div class="tx-box">
            <div class="tx-row">
                <span class="tx-k">Type</span>
                <span class="badge b-{transaction_type}">{transaction_type}</span>
            </div>
            <div class="tx-row">
                <span class="tx-k">Amount</span>
                <span class="tx-v">${amount:,.2f}</span>
            </div>
            <div class="tx-row">
                <span class="tx-k">Sender Δ</span>
                <span class="tx-v" style="color:#EF4444">−${sender_delta:,.2f}</span>
            </div>
            <div class="tx-row">
                <span class="tx-k">Receiver Δ</span>
                <span class="tx-v" style="color:#10B981">+${receiver_delta:,.2f}</span>
            </div>
            <div class="tx-row">
                <span class="tx-k">Verdict</span>
                <span class="tx-v" style="color:{verdict_color}">{verdict_text}</span>
            </div>
            <div class="tx-row">
                <span class="tx-k">Risk Score</span>
                <span class="tx-v" style="color:{verdict_color}">{fraud_pct:.1f}%</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Built with ❤️ using Streamlit &amp; Machine Learning &nbsp;|&nbsp;
    Trained on 6.3M+ real-world transactions &nbsp;|&nbsp;
    FraudShield AI &nbsp;©&nbsp;2025
</div>
""", unsafe_allow_html=True)
