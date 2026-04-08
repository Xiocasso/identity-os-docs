"""Generate PDF of the stress model workshop paper."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether,
)
from reportlab.lib.colors import HexColor, black, grey
from reportlab.lib import colors

import os

OUTPUT_DIR = "/sessions/dazzling-friendly-bohr/mnt/Identity OS"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Stress-Adaptive-Action-Governance-Paper.pdf")


def build_styles():
    """Build custom paragraph styles for academic paper."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'PaperTitle',
        parent=styles['Title'],
        fontSize=16,
        leading=20,
        alignment=TA_CENTER,
        spaceAfter=6,
        fontName='Times-Bold',
    ))
    styles.add(ParagraphStyle(
        'PaperAuthor',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        alignment=TA_CENTER,
        spaceAfter=18,
        fontName='Times-Italic',
    ))
    styles.add(ParagraphStyle(
        'SectionHead',
        parent=styles['Heading1'],
        fontSize=13,
        leading=16,
        spaceBefore=16,
        spaceAfter=8,
        fontName='Times-Bold',
    ))
    styles.add(ParagraphStyle(
        'SubsectionHead',
        parent=styles['Heading2'],
        fontSize=11,
        leading=14,
        spaceBefore=12,
        spaceAfter=6,
        fontName='Times-Bold',
    ))
    styles.add(ParagraphStyle(
        'SubsubHead',
        parent=styles['Heading3'],
        fontSize=10,
        leading=13,
        spaceBefore=8,
        spaceAfter=4,
        fontName='Times-BoldItalic',
    ))
    styles.add(ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
        fontName='Times-Roman',
        firstLineIndent=18,
    ))
    styles.add(ParagraphStyle(
        'BodyFirst',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
        fontName='Times-Roman',
        firstLineIndent=0,
    ))
    styles.add(ParagraphStyle(
        'AbstractLabel',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        alignment=TA_CENTER,
        spaceAfter=4,
        fontName='Times-Bold',
    ))
    styles.add(ParagraphStyle(
        'AbstractText',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        fontName='Times-Italic',
        leftIndent=36,
        rightIndent=36,
    ))
    styles.add(ParagraphStyle(
        'Equation',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        spaceAfter=8,
        spaceBefore=8,
        fontName='Times-Italic',
    ))
    styles.add(ParagraphStyle(
        'BulletItem',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        alignment=TA_JUSTIFY,
        spaceAfter=3,
        fontName='Times-Roman',
        leftIndent=36,
        bulletIndent=18,
    ))
    styles.add(ParagraphStyle(
        'RefEntry',
        parent=styles['Normal'],
        fontSize=8.5,
        leading=11,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
        fontName='Times-Roman',
        leftIndent=18,
        firstLineIndent=-18,
    ))
    styles.add(ParagraphStyle(
        'AppendixBody',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        alignment=TA_JUSTIFY,
        spaceAfter=5,
        fontName='Times-Roman',
    ))
    return styles


def make_table(headers, rows, col_widths=None):
    """Create a formatted table."""
    data = [headers] + rows
    if col_widths is None:
        col_widths = [None] * len(headers)

    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('LEADING', (0, 0), (-1, -1), 12),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 3),
        ('TOPPADDING', (0, 1), (-1, -1), 3),
        ('LINEBELOW', (0, 0), (-1, 0), 1, black),
        ('LINEABOVE', (0, 0), (-1, 0), 1, black),
        ('LINEBELOW', (0, -1), (-1, -1), 1, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def build_paper():
    """Build the full paper PDF."""
    styles = build_styles()

    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        leftMargin=1.0 * inch,
        rightMargin=1.0 * inch,
    )

    story = []

    # ── Title ──
    story.append(Paragraph(
        "Stress-Adaptive Action Governance<br/>for Autonomous AI Agents",
        styles['PaperTitle'],
    ))
    story.append(Paragraph("Anonymous Authors", styles['PaperAuthor']))

    # ── Abstract ──
    story.append(Paragraph("Abstract", styles['AbstractLabel']))
    story.append(Paragraph(
        "Current approaches to AI agent safety rely primarily on static guardrails "
        "\u2014 fixed allow/deny lists that either block forbidden actions or permit everything "
        "else, regardless of situational context. We present a stress-adaptive governance model "
        "that dynamically restricts an agent\u2019s action vocabulary in response to environmental "
        "pressure. The model defines four stress levels (LOW, MED, HIGH, OVER) that progressively "
        "tighten behavioral constraints through a deterministic pipeline: observations activate "
        "behavioral modes via exponential moving averages, mode activation drives stress "
        "classification, and stress level determines the set of actions available to the agent "
        "at each decision cycle. Under extreme stress (OVER), the agent\u2019s action space collapses "
        "to a minimal safe set of four reactive and disengagement actions. We evaluate this model "
        "against a static action filter baseline across four scenarios totaling 1,200 decision "
        "cycles. In the stress-spike scenario, the adaptive model escalates through all four "
        "levels, restricts the average action space from 12 to ~6 actions, and spends 58 turns "
        "in HIGH or OVER states \u2014 while the static baseline remains permanently at LOW with "
        "all 12 actions available. Both systems achieve identical forbidden-action blocking (100%), "
        "demonstrating that the adaptive model\u2019s advantage lies not in what it blocks, but in "
        "how it governs what remains permitted. We argue that stress-adaptive governance addresses "
        "a critical gap between static guardrails and unconstrained agent autonomy.",
        styles['AbstractText'],
    ))

    # ── 1. Introduction ──
    story.append(Paragraph("1. Introduction", styles['SectionHead']))

    story.append(Paragraph(
        "The deployment of autonomous AI agents \u2014 systems that take actions in external "
        "environments based on language model reasoning \u2014 has created an urgent need for "
        "runtime behavioral governance. Current safety approaches fall into two broad "
        "categories. The first is prompt-level guardrails: system instructions, constitutional "
        "principles, or RLHF training that attempt to shape the model\u2019s behavior before "
        "deployment. These approaches are well-studied but fundamentally brittle; they operate "
        "at the level of token generation and can be bypassed through adversarial prompting, "
        "context manipulation, or simply through the stochastic nature of language model "
        "sampling (Perez et al., 2022; Wei et al., 2023).",
        styles['BodyFirst'],
    ))

    story.append(Paragraph(
        "The second category is framework-level middleware: runtime systems that intercept "
        "agent actions and apply allow/deny rules. Tools like Guardrails AI (2023) and NVIDIA "
        "NeMo Guardrails (Rebedea et al., 2023) exemplify this approach. They provide "
        "deterministic enforcement \u2014 a forbidden action is always blocked \u2014 but they are "
        "fundamentally static. A static filter applies the same permissions whether the agent "
        "is operating normally or is under severe environmental pressure. It cannot distinguish "
        "between a routine decision cycle and one where the agent\u2019s behavioral state suggests "
        "it should be operating with extreme caution.",
        styles['Body'],
    ))

    story.append(Paragraph(
        "This paper addresses the gap between these two approaches. We present a stress-adaptive "
        "governance model that sits at the middleware layer but responds dynamically to the "
        "agent\u2019s behavioral state. The core insight is straightforward: <b>the set of actions "
        "an agent should be permitted to take is not fixed, but should vary based on the agent\u2019s "
        "current stress level.</b> An agent operating under normal conditions may safely take "
        "proactive actions \u2014 exploring new directions, challenging assumptions, or changing "
        "approach. An agent under extreme stress should be restricted to reactive and "
        "disengagement actions only \u2014 regardless of what the underlying language model "
        "might prefer to do.",
        styles['Body'],
    ))

    story.append(Paragraph("Our contributions are:", styles['BodyFirst']))

    story.append(Paragraph(
        "<bullet>&bull;</bullet> A formal stress model with four levels (LOW, MED, HIGH, OVER) "
        "that deterministically maps environmental signals to action-space constraints, with a "
        "complete causal chain from observation to contract output.",
        styles['BulletItem'],
    ))
    story.append(Paragraph(
        "<bullet>&bull;</bullet> Empirical evaluation across 1,200 decision cycles (4 scenarios "
        "\u00d7 300 turns) comparing the adaptive model against a static action filter baseline, "
        "demonstrating that the systems are equivalent on forbidden-action blocking but diverge "
        "significantly on permitted-action governance.",
        styles['BulletItem'],
    ))
    story.append(Paragraph(
        "<bullet>&bull;</bullet> Evidence from adversarial testing showing 100% forbidden-action "
        "blocking with the middleware versus 100% execution without it, across both LangGraph "
        "and CrewAI integration frameworks.",
        styles['BulletItem'],
    ))

    # ── 2. Related Work ──
    story.append(Paragraph("2. Related Work", styles['SectionHead']))

    story.append(Paragraph(
        "<b>Prompt-level safety.</b> Constitutional AI (Bai et al., 2022) embeds behavioral "
        "principles during training; the model learns to self-critique and revise outputs that "
        "violate its constitution. This operates at the model level and cannot enforce "
        "constraints at runtime once the model has been deployed as an agent. Reinforcement "
        "Learning from Human Feedback (Ouyang et al., 2022) similarly shapes behavior during "
        "training but provides no runtime guarantees.",
        styles['BodyFirst'],
    ))

    story.append(Paragraph(
        "<b>Static guardrails.</b> Guardrails AI provides a validation framework that checks "
        "LLM outputs against predefined schemas and rules. NeMo Guardrails (Rebedea et al., "
        "2023) uses a dialog management approach to enforce conversational boundaries. Both "
        "systems operate on a fixed rule set: an action is either permitted or forbidden, "
        "independent of the agent\u2019s current behavioral state. They provide necessary but not "
        "sufficient safety \u2014 they prevent known-bad actions but do not adaptively govern the "
        "space of permitted actions.",
        styles['Body'],
    ))

    story.append(Paragraph(
        "<b>Cognitive architectures.</b> ACT-R (Anderson et al., 2004) and SOAR (Laird, 2012) "
        "model stress and cognitive load in human cognition simulations. These systems inform "
        "our design but target a fundamentally different problem: simulating human psychology "
        "rather than governing AI agent behavior. Recent work on cognitive architectures for "
        "LLM agents (Sumers et al., 2023) explores similar structural patterns but does not "
        "address runtime stress governance.",
        styles['Body'],
    ))

    story.append(Paragraph(
        "<b>Agent safety frameworks.</b> Recent surveys of LLM agent risks (Ruan et al., 2024; "
        "Xi et al., 2023) identify action safety as a key concern but focus on risk taxonomies "
        "rather than runtime mitigation mechanisms. The AgentBench benchmark (Liu et al., 2023) "
        "evaluates agent capabilities but does not measure governance or constraint behavior.",
        styles['Body'],
    ))

    story.append(Paragraph(
        "To our knowledge, no prior work implements stress as a runtime governance mechanism "
        "that dynamically restricts an AI agent\u2019s action vocabulary based on environmental "
        "pressure signals.",
        styles['Body'],
    ))

    # ── 3. Stress-Adaptive Governance Model ──
    story.append(Paragraph("3. Stress-Adaptive Governance Model", styles['SectionHead']))

    story.append(Paragraph("3.1 Overview", styles['SubsectionHead']))
    story.append(Paragraph(
        "The governance model operates as middleware between the agent framework (e.g., "
        "LangGraph, CrewAI) and the language model. At each decision cycle, the agent sends "
        "an observation to the middleware, which processes it through a deterministic pipeline "
        "and returns an <b>execution contract</b> \u2014 a read-only specification of what the "
        "agent is permitted to do.",
        styles['BodyFirst'],
    ))
    story.append(Paragraph(
        "The pipeline consists of seven stages: (1) mode activation, (2) energy update, "
        "(3) stress and state evaluation, (4) arbitration, (5) composite detection, "
        "(6) drift detection, and (7) stability computation. For the purpose of this paper, "
        "we focus on stages 1, 3, and the contract output, which together constitute the "
        "stress-adaptive governance mechanism.",
        styles['Body'],
    ))

    story.append(Paragraph("3.2 Mode Activation", styles['SubsectionHead']))
    story.append(Paragraph(
        "The system maintains a vector of seven behavioral modes, each representing a "
        "dimension of agent behavior (e.g., perception, exploration, order, assertion, "
        "connection). Each observation targets a specific mode and carries a signal strength "
        "and confidence value.",
        styles['BodyFirst'],
    ))
    story.append(Paragraph(
        "Mode values are updated using an exponential moving average (EMA):",
        styles['Body'],
    ))
    story.append(Paragraph(
        "v<sub>t+1</sub>(m) = v<sub>t</sub>(m) \u00b7 (1 \u2212 \u03b1 \u00b7 c) + s \u00b7 \u03b1 \u00b7 c",
        styles['Equation'],
    ))
    story.append(Paragraph(
        "where v<sub>t</sub>(m) is the current value for mode m, s is the signal strength, "
        "c is the confidence, and \u03b1 is the base learning rate. Only the targeted mode is "
        "updated per cycle; all other modes retain their previous values.",
        styles['BodyFirst'],
    ))
    story.append(Paragraph(
        "One of the seven modes is designated as the <b>stress response</b> mode. When the "
        "environment produces distress signals \u2014 blocked actions, errors, conflicting data, "
        "resource contention \u2014 these manifest as high-strength observations targeting the "
        "stress response mode.",
        styles['Body'],
    ))

    story.append(Paragraph("3.3 Stress Classification", styles['SubsectionHead']))
    story.append(Paragraph(
        "The absolute value of the stress response mode determines the agent\u2019s stress level "
        "via threshold comparison. Four ordered thresholds \u03b8<sub>med</sub> &lt; "
        "\u03b8<sub>high</sub> &lt; \u03b8<sub>over</sub> partition the stress value into "
        "levels LOW, MED, HIGH, and OVER. Because the stress response mode is updated via EMA, "
        "stress level changes are smooth rather than abrupt \u2014 a single high-stress observation "
        "does not immediately push the system to OVER; sustained pressure is required.",
        styles['BodyFirst'],
    ))

    story.append(Paragraph("3.4 System State Transitions", styles['SubsectionHead']))
    story.append(Paragraph(
        "The stress level feeds into a three-state system state machine: BASELINE, GROWTH, and "
        "STRESS. The system enters the STRESS state when the stress level reaches HIGH or OVER. "
        "It does not exit immediately when stress subsides; instead, it requires k consecutive "
        "calm cycles before transitioning back to BASELINE. This hysteresis prevents oscillation "
        "between states during noisy environments.",
        styles['BodyFirst'],
    ))

    story.append(Paragraph("3.5 Action Space Governance", styles['SubsectionHead']))
    story.append(Paragraph(
        "The execution contract\u2019s permitted action set is determined by which behavioral modes "
        "are currently active (above a threshold). Each active mode contributes a subset of "
        "actions to the permitted set. Under normal conditions, multiple active modes produce "
        "a rich action vocabulary.",
        styles['BodyFirst'],
    ))
    story.append(Paragraph(
        "Under OVER stress, this mode-driven mechanism is overridden entirely. The permitted "
        "action set collapses to a fixed safe set A<sub>OVER</sub> containing only 4 actions "
        "drawn from the reactive and disengagement categories. This override is unconditional: "
        "regardless of which modes are active or what the language model prefers, the agent is "
        "restricted to these four actions until stress subsides. No proactive actions are "
        "available under OVER.",
        styles['Body'],
    ))
    story.append(Paragraph(
        "The system also produces <b>forbidden actions</b> \u2014 actions that are never "
        "permitted regardless of stress level. These are statically defined and function "
        "identically to a traditional static guardrail. The stress model governs the space "
        "between \u201calways forbidden\u201d and \u201calways allowed.\u201d",
        styles['Body'],
    ))

    story.append(Paragraph("3.6 Energy Coupling", styles['SubsectionHead']))
    story.append(Paragraph(
        "Stress affects the agent\u2019s energy model. During the STRESS system state, per-cycle "
        "energy cost increases due to stress overhead, while the recovery rate drops. This "
        "creates a secondary pressure: sustained stress depletes the agent\u2019s operational "
        "capacity, providing an additional signal to the agent framework that the agent needs "
        "recovery time.",
        styles['BodyFirst'],
    ))

    story.append(Paragraph("3.7 Causal Traceability", styles['SubsectionHead']))
    story.append(Paragraph(
        "A key design property is that every contract output is deterministically traceable to "
        "its inputs. Given an observation sequence, one can reconstruct the exact state "
        "trajectory and verify why a particular action was permitted or restricted at any turn. "
        "There is no stochastic sampling or LLM inference in the governance pipeline. This "
        "property is critical for auditability in production deployments.",
        styles['BodyFirst'],
    ))

    # ── 4. Empirical Evaluation ──
    story.append(Paragraph("4. Empirical Evaluation", styles['SectionHead']))

    story.append(Paragraph("4.1 Experimental Setup", styles['SubsectionHead']))
    story.append(Paragraph(
        "We evaluate the stress-adaptive model against a <b>static action filter</b> baseline. "
        "The static filter implements the simplest reasonable alternative: all 12 standard "
        "actions are always permitted, and 2 forbidden actions are always blocked. It has no "
        "stress model, no energy tracking, and no drift detection.",
        styles['BodyFirst'],
    ))
    story.append(Paragraph(
        "Both systems are evaluated on four scenarios, each running for 300 decision cycles: "
        "(A) Steady State \u2014 consistent signals, no perturbation; "
        "(B) Gradual Shift \u2014 signals slowly change over 300 turns; "
        "(C) Stress Spike \u2014 sudden high-intensity stress at mid-session; "
        "(D) Chaotic \u2014 random modes, noise injection, adversarial signals. "
        "Observations are generated synthetically using seeded random number generators.",
        styles['Body'],
    ))

    story.append(Paragraph("4.2 Results", styles['SubsectionHead']))

    story.append(Paragraph("4.2.1 Forbidden Action Blocking", styles['SubsubHead']))
    story.append(Paragraph(
        "Both systems achieve identical forbidden-action blocking across all scenarios: "
        "48/48 attempts caught in each scenario, 192/192 total. This is expected \u2014 "
        "forbidden-action blocking is a static property independent of stress level.",
        styles['BodyFirst'],
    ))

    story.append(Paragraph("4.2.2 Action Space Governance", styles['SubsubHead']))
    story.append(Paragraph(
        "The systems diverge sharply on how they govern permitted actions:",
        styles['BodyFirst'],
    ))
    story.append(Spacer(1, 4))

    t1 = make_table(
        ['Scenario', 'Adaptive Avg', 'Static Avg', 'Restricted Turns'],
        [
            ['Steady State (A)', '5.04', '12.0', '298/300'],
            ['Gradual Shift (B)', '4.84', '12.0', '299/300'],
            ['Stress Spike (C)', '5.89', '12.0', '298/300'],
            ['Chaotic (D)', '10.03', '12.0', '223/300'],
        ],
        col_widths=[1.8 * inch, 1.2 * inch, 1.1 * inch, 1.3 * inch],
    )
    story.append(t1)
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "The static filter always permits all 12 actions. The adaptive model restricts the "
        "action space in the vast majority of turns \u2014 not because it is blocking "
        "\u201cbad\u201d actions, but because it is governing what actions are contextually "
        "appropriate given the agent\u2019s current behavioral state.",
        styles['BodyFirst'],
    ))

    story.append(Paragraph("4.2.3 Stress Model Behavior", styles['SubsubHead']))
    story.append(Paragraph(
        "The stress spike scenario (C) provides the clearest demonstration:",
        styles['BodyFirst'],
    ))
    story.append(Spacer(1, 4))

    t2 = make_table(
        ['Metric', 'Adaptive', 'Static'],
        [
            ['Max stress level', 'OVER', 'LOW (no model)'],
            ['Stress escalations', '3', '0'],
            ['Turns at HIGH/OVER', '58', '0'],
            ['Min allowed actions', '3', '12'],
        ],
        col_widths=[2.2 * inch, 1.5 * inch, 1.7 * inch],
    )
    story.append(t2)
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "The adaptive model detects the stress spike, escalates through LOW \u2192 MED \u2192 "
        "HIGH \u2192 OVER, restricts the action space to the safe set, and then gradually "
        "recovers as stress signals subside. In the chaotic scenario (D), the adaptive model "
        "reaches MED stress with 2 escalations but does not reach HIGH or OVER, demonstrating "
        "appropriate proportionality.",
        styles['BodyFirst'],
    ))

    story.append(Paragraph("4.2.4 Adversarial Enforcement", styles['SubsubHead']))
    story.append(Paragraph(
        "We additionally tested a rebellious agent \u2014 one programmed to attempt only "
        "forbidden actions \u2014 across two integration frameworks:",
        styles['BodyFirst'],
    ))
    story.append(Spacer(1, 4))

    t3 = make_table(
        ['Framework', 'Turns', 'With Middleware', 'Without'],
        [
            ['LangGraph', '100', '100/100 blocked', '100/100 executed'],
            ['CrewAI', '50', '50/50 blocked', '50/50 executed'],
        ],
        col_widths=[1.4 * inch, 0.9 * inch, 1.6 * inch, 1.5 * inch],
    )
    story.append(t3)
    story.append(Spacer(1, 6))

    story.append(Paragraph("4.3 Integration Architecture", styles['SubsectionHead']))
    story.append(Paragraph(
        "The governance model integrates with existing agent frameworks through "
        "framework-specific adapters. In LangGraph, a guard node is inserted into the agent\u2019s "
        "state graph; in CrewAI, a guardrail callback is attached to the task execution "
        "pipeline. In both cases, the agent framework is unmodified. The governance model "
        "operates as pure middleware \u2014 it reads observations and writes contracts, but never "
        "modifies the agent\u2019s internal state or the language model\u2019s outputs directly.",
        styles['BodyFirst'],
    ))

    # ── 5. Discussion ──
    story.append(Paragraph("5. Discussion", styles['SectionHead']))

    story.append(Paragraph("5.1 Why Adaptive Governance Matters", styles['SubsectionHead']))
    story.append(Paragraph(
        "The key finding is not that the adaptive model blocks more forbidden actions \u2014 both "
        "systems achieve 100% on that metric. The finding is that the adaptive model <b>governs "
        "the entire permitted action space</b> based on situational awareness.",
        styles['BodyFirst'],
    ))
    story.append(Paragraph(
        "Consider a production scenario: an agent managing customer support encounters a cascade "
        "of errors \u2014 API failures, conflicting database records, timeout exceptions. A static "
        "guardrail sees nothing unusual; all proposed actions are technically permitted. The "
        "adaptive model recognizes the accumulating stress, escalates to HIGH or OVER, and "
        "restricts the agent to reactive and disengagement actions only \u2014 preventing the agent "
        "from taking aggressive actions during a crisis it may not fully understand.",
        styles['Body'],
    ))

    story.append(Paragraph("5.2 Determinism as a Safety Property", styles['SubsectionHead']))
    story.append(Paragraph(
        "The entire pipeline from observation to contract is deterministic and contains no LLM "
        "inference. This means: (1) <b>Auditability</b> \u2014 given an observation log, any "
        "contract output can be exactly reproduced; (2) <b>Predictability</b> \u2014 the system\u2019s "
        "behavior under any input sequence is fully determined by its parameters; (3) "
        "<b>Testability</b> \u2014 the stress model can be exhaustively tested with synthetic "
        "scenarios. This contrasts with prompt-level approaches where the same safety instruction "
        "can produce different behaviors across runs.",
        styles['BodyFirst'],
    ))

    story.append(Paragraph("5.3 The OVER Lockdown", styles['SubsectionHead']))
    story.append(Paragraph(
        "The OVER state represents the model\u2019s strongest safety guarantee: under extreme stress, "
        "the agent is restricted to only 4 reactive and disengagement actions. We argue this is "
        "the correct default. An agent under extreme stress is, by definition, operating in "
        "conditions it was not designed for. The OVER lockdown provides a deterministic floor: "
        "no matter how badly the environment deteriorates, the agent cannot take aggressive, "
        "exploratory, or challenging actions.",
        styles['BodyFirst'],
    ))

    story.append(Paragraph("5.4 Limitations", styles['SubsectionHead']))
    story.append(Paragraph(
        "<b>Energy model coupling.</b> The energy model depletes to zero under sustained stress "
        "and recovers slowly. In the stress spike scenario, 167 out of 300 turns have energy at "
        "the critical threshold. While this does not affect the stress escalation chain (which is "
        "driven by mode activation, not energy), it means the energy signal may be less useful "
        "than intended during recovery. This is a tuning issue we are actively addressing.",
        styles['BodyFirst'],
    ))
    story.append(Paragraph(
        "<b>No user study.</b> We demonstrate that the stress model behaves as designed "
        "(deterministic verification) but do not measure whether stress-governed agents produce "
        "better outcomes for end users. A controlled user study comparing agent performance with "
        "and without stress-adaptive governance is needed.",
        styles['Body'],
    ))
    story.append(Paragraph(
        "<b>Single-system evaluation.</b> All results are from our implementation. While the "
        "stress model is framework-agnostic in design, we have not evaluated it in third-party "
        "governance systems.",
        styles['Body'],
    ))
    story.append(Paragraph(
        "<b>Drift detection maturity.</b> The system includes a drift detection module (not the "
        "focus of this paper) that achieves an aggregate F1 of 0.248 in ground-truth evaluation "
        "\u2014 insufficient for production use as a primary safety mechanism. The stress model "
        "does not depend on drift detection for its operation.",
        styles['Body'],
    ))

    # ── 6. Conclusion ──
    story.append(Paragraph("6. Conclusion", styles['SectionHead']))
    story.append(Paragraph(
        "We have presented a stress-adaptive governance model for autonomous AI agents that "
        "dynamically restricts action vocabulary based on environmental pressure. The model "
        "addresses a gap between static guardrails (which block forbidden actions but do not "
        "govern permitted ones) and unconstrained agent autonomy. Our empirical evaluation "
        "demonstrates that the model provides deterministic, traceable, and proportional stress "
        "response across diverse scenarios while maintaining identical forbidden-action blocking "
        "to a static baseline.",
        styles['BodyFirst'],
    ))
    story.append(Paragraph(
        "The stress model\u2019s key properties \u2014 deterministic causality, graduated response, and "
        "unconditional OVER lockdown \u2014 make it suitable for production deployments where "
        "auditability and predictability are requirements. We release the governance model as "
        "part of an open-source behavioral middleware system and invite the community to evaluate "
        "its applicability to their agent safety needs.",
        styles['Body'],
    ))

    # ── References ──
    story.append(Paragraph("References", styles['SectionHead']))

    refs = [
        "Anderson, J. R., Bothell, D., Byrne, M. D., Douglass, S., Lebiere, C., &amp; Qin, Y. (2004). An integrated theory of the mind. <i>Psychological Review</i>, 111(4), 1036\u20131060.",
        "Bai, Y., Jones, A., Ndousse, K., et al. (2022). Training a helpful and harmless assistant with reinforcement learning from human feedback. <i>arXiv:2204.05862</i>.",
        "Guardrails AI. (2023). Guardrails: Adding guardrails to large language models. github.com/guardrails-ai/guardrails",
        "Laird, J. E. (2012). <i>The Soar Cognitive Architecture</i>. MIT Press.",
        "Liu, X., Yu, H., Zhang, H., et al. (2023). AgentBench: Evaluating LLMs as agents. <i>arXiv:2308.03688</i>.",
        "Ouyang, L., Wu, J., Jiang, X., et al. (2022). Training language models to follow instructions with human feedback. <i>NeurIPS</i>, 35.",
        "Perez, E., Ringer, S., Lukosiute, K., et al. (2022). Red teaming language models with language models. <i>arXiv:2202.03286</i>.",
        "Rebedea, T., Dinu, R., Sreedhar, M., Parisien, C., &amp; Cohen, J. (2023). NeMo Guardrails: A toolkit for controllable and safe LLM applications. <i>arXiv:2310.10501</i>.",
        "Ruan, Y., Dong, H., Wang, A., et al. (2024). Identifying the risks of LM agents with an LM-emulated sandbox. <i>arXiv:2309.15817</i>.",
        "Sumers, T. R., Yao, S., Narasimhan, K., &amp; Griffiths, T. L. (2023). Cognitive architectures for language agents. <i>arXiv:2309.02427</i>.",
        "Wei, A., Haghtalab, N., &amp; Steinhardt, J. (2023). Jailbroken: How does LLM safety training fail? <i>arXiv:2307.02483</i>.",
        "Xi, Z., Chen, W., Guo, X., et al. (2023). The rise and potential of large language model based agents: A survey. <i>arXiv:2309.07864</i>.",
    ]
    for ref in refs:
        story.append(Paragraph(ref, styles['RefEntry']))

    # ── Appendix ──
    story.append(PageBreak())
    story.append(Paragraph("Appendix A: Action Taxonomy", styles['SectionHead']))
    story.append(Paragraph(
        "The system defines a vocabulary of |A| = 12 standard actions spanning proactive "
        "behaviors (e.g., initiating exploration, proposing changes), reactive behaviors "
        "(e.g., responding to queries, maintaining stability), and disengagement behaviors "
        "(e.g., deferring decisions, withdrawing from activity). Two additional actions are "
        "permanently forbidden regardless of stress level.",
        styles['AppendixBody'],
    ))
    story.append(Paragraph(
        "Under OVER stress, only a safe subset of 4 actions is permitted. These 4 actions are "
        "drawn exclusively from the reactive and disengagement categories \u2014 no proactive "
        "actions are available. This ensures the agent cannot initiate new activity during a "
        "crisis.",
        styles['AppendixBody'],
    ))

    story.append(Paragraph("Appendix B: Scenario Specifications", styles['SectionHead']))
    story.append(Paragraph(
        "<b>Steady State (A):</b> 300 turns. Single mode targeted per turn with moderate signal "
        "strength (0.3\u20130.7) and high confidence (0.7\u20130.9). Mode selection cycles through "
        "non-stress modes.",
        styles['AppendixBody'],
    ))
    story.append(Paragraph(
        "<b>Gradual Shift (B):</b> 300 turns. Initial 100 turns target perception/order modes; "
        "turns 100\u2013200 shift toward exploration/assertion; turns 200\u2013300 shift toward "
        "connection/identity. Signal strengths increase linearly from 0.3 to 0.8.",
        styles['AppendixBody'],
    ))
    story.append(Paragraph(
        "<b>Stress Spike (C):</b> 300 turns. Normal signals for turns 0\u201399. Turns 100\u2013149: "
        "high-intensity (0.8\u20131.0) stress response signals. Turns 150\u2013299: return to normal "
        "signals. Tests escalation and recovery.",
        styles['AppendixBody'],
    ))
    story.append(Paragraph(
        "<b>Chaotic (D):</b> 300 turns. Each turn randomly selects a mode (including stress "
        "response), signal strength (0.1\u20131.0), and confidence (0.3\u20131.0) from a uniform "
        "distribution.",
        styles['AppendixBody'],
    ))

    doc.build(story)
    print(f"PDF generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_paper()
