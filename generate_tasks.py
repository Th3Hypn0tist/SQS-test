import json
import random
random.seed(1)


def mc_question(qid, difficulty, question, options, correct_index):
    return {
        "id": qid,
        "difficulty": difficulty,
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correctIndex": correct_index,
    }


def num_question(qid, difficulty, question, correct_value):
    return {
        "id": qid,
        "difficulty": difficulty,
        "type": "numeric",
        "question": question,
        "correctValue": correct_value,
    }


def write_file(name, data):
    with open(name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ---------- Fractal Learning ----------

def generate_fl_tasks():
    tasks = []
    analogies = [
        ("FL-1", "Shape edges: triangle:3 :: hexagon:?", ["5", "6", "7", "8"], 1),
        ("FL-2", "Letter steps: A, C, F, J, ? (gaps grow by +1)", ["N", "O", "P", "Q"], 0),
        ("FL-3", "Symbol echo: X, XY, XYY, XYYY, next Y count?", ["4", "5", "6", "7"], 0),
        ("FL-4", "Pair growth: (1→2), (2→5), (3→10), (4→17). Output for 5?", ["24", "25", "26", "27"], 2),
        ("FL-5", "Nested brackets: [], [()], [(){}], [(){}<>]. Next pair added?", ["[]", "()", "{}", "<>"], 3),
        ("FL-6", "Sequence: 1, 3, 7, 15, ? (double then +1)", ["23", "27", "31", "33"], 2),
        ("FL-7", "Mirror counts: ⭕, ⭕⭕, ⭕⭕⭕, step 5 has how many rings?", ["4", "5", "6", "7"], 1),
        ("FL-8", "Split mapping: A→AB, B→BA. After ABBA, length of next string?", ["6", "8", "10", "12"], 2),
        ("FL-9", "Alternating add/multiply: 2, 4, 12, 14, 42, ?. Next term?", ["44", "84", "126", "170"], 2),
        ("FL-10", "Simple analogy: north:south :: ascend: ?", ["climb", "descend", "pause", "rotate"], 1),
    ]
    for qid, text, opts, correct_idx in analogies:
        tasks.append(mc_question(qid, 1, text, opts, correct_idx))

    for i in range(11, 31):
        base = i - 10
        seq = [base, base * 2 + 1, base * 3 + 2]
        next_val = base * 4 + 3
        tasks.append(num_question(f"FL-{i}", 2, f"Layered growth {base}: {seq[0]}, {seq[1]}, {seq[2]}, ?. Pattern adds base then +1 each step.", next_val))

    for i in range(31, 41):
        step = i - 30
        a = 2 + step
        b = a * 2 + step
        c = b * 2 - step
        next_val = c + step * 2
        options = [next_val - step, next_val, next_val + step, next_val + 2 * step]
        tasks.append(mc_question(f"FL-{i}", 3, f"Hybrid rule {step}: start {a}, then ×2+{step}, then ×2−{step}. Next value?", [str(o) for o in options], 1))

    for i in range(41, 51):
        shift = i - 40
        values = [shift]
        inc = 1
        for _ in range(3):
            inc += shift
            values.append(values[-1] + inc)
        next_val = values[-1] - (shift - 1) + 2 * shift
        options = [next_val - shift, next_val, next_val + shift, next_val + 2 * shift]
        tasks.append(mc_question(f"FL-{i}", 4, f"Increment chain {values} then switch: subtract {shift-1}, add {2*shift}. Next value?", [str(o) for o in options], 1))
    return tasks


# ---------- Recursive Reasoning ----------

def generate_rr_tasks():
    tasks = []
    for i in range(1, 11):
        start = i + 1
        question = f"Iterate f(x)=x+2 for 3 steps starting at {start}. Result?"
        result = start + 6
        options = [result - 2, result - 1, result, result + 1]
        tasks.append(mc_question(f"RR-{i}", 1, question, [str(o) for o in options], 2))

    for i in range(11, 31):
        start = (i % 7) + 3
        steps = 3
        val = start
        log = []
        for _ in range(steps):
            if val % 2 == 0:
                val = val // 2 + 3
                log.append('even→half+3')
            else:
                val = val * 2 - 1
                log.append('odd→double−1')
        tasks.append(num_question(f"RR-{i}", 2, f"State machine start {start}; rules {', '.join(log)}. Final value?", val))

    for i in range(31, 41):
        depth = 4
        start = 3 + (i - 31)
        def g(x, d):
            if d == 0:
                return x
            if x % 3 == 0:
                return g(x // 3 + d, d - 1)
            if x % 3 == 1:
                return g(x * 2 + d, d - 1)
            return g(x + 5, d - 1)
        result = g(start, depth)
        tasks.append(num_question(f"RR-{i}", 3, f"Recursive branching depth {depth} starting at {start} with mod-3 rules. Final value?", result))

    for i in range(41, 51):
        start = 5 + (i - 41)
        def h(x, d):
            if d == 0:
                return x
            if d % 2 == 0:
                nxt = x + d + (1 if x % 2 else -1)
            else:
                nxt = x * 2 - d + (2 if x % 3 == 0 else -2)
            return h(nxt, d - 1)
        result = h(start, 5)
        tasks.append(num_question(f"RR-{i}", 4, f"Nested recursion depth 5 starting {start}. Even depths add, odd depths double then adjust. Final value?", result))
    return tasks


# ---------- Multidomain Flexibility ----------

def generate_mf_tasks():
    tasks = []
    analogies = [
        ("MF-1", "Bridge : river :: Router : ?", ["Signal", "Packet", "Cable", "Switch"], 1),
        ("MF-2", "Skeleton : body :: Framework : ?", ["Detail", "Template", "Decoration", "Surface"], 1),
        ("MF-3", "Filter : noise :: Gate : ?", ["Entry", "Flow", "Barrier", "Signal"], 1),
        ("MF-4", "Index : book :: Map : ?", ["Route", "Compass", "Legend", "Key"], 3),
        ("MF-5", "Lens : focus :: Protocol : ?", ["Sequence", "Priority", "Clarity", "Boundary"], 2),
        ("MF-6", "Outline : essay :: Blueprint : ?", ["Material", "Structure", "Worker", "Budget"], 1),
        ("MF-7", "Pivot : table :: Hub : ?", ["Spoke", "Node", "Center", "Edge"], 2),
        ("MF-8", "Scaffold : building :: Schema : ?", ["Data", "Format", "Record", "Column"], 1),
        ("MF-9", "Heartbeat : rhythm :: Clock : ?", ["Alarm", "Tick", "Chime", "Face"], 1),
        ("MF-10", "Valve : flow :: Moderator : ?", ["Rule", "Heat", "Volume", "Access"], 3),
    ]
    for qid, text, opts, ci in analogies:
        tasks.append(mc_question(qid, 1, text, opts, ci))

    for i in range(11, 31):
        span = (i - 10) % 5 + 2
        sequence = "O " + "L " * span
        question = f"Grid constraint scenario {i-10}: hallway pattern repeats '{sequence.strip()}'. Which sequence lets a mover advance every third step?"
        options = [
          f"{sequence.strip()} {sequence.strip()}",
          "O O L O O L",
          "L O L L O L",
          "O L O L O L",
        ]
        tasks.append(mc_question(f"MF-{i}", 2, question, options, 3 if span % 2 ==0 else 1))

    for i in range(31, 41):
        arrivals = 3 + (i - 31)
        question = f"Three domains align queues with priority to newest then alternate for {arrivals} arrivals. Which policy matches?"
        options = [
            "Always FIFO",
            "Priority to newest then alternate",
            "Strict round-robin",
            "Random selection",
        ]
        tasks.append(mc_question(f"MF-{i}", 3, question, options, 1))

    for i in range(41, 51):
        layer = i - 40
        question = f"Cross-domain fixed-point alignment layer {layer}: planning, scheduling, layout iterate until constraints stop shifting. Which strategy matches?"
        options = [
            "Iterate adjustments until no conflicts remain",
            "Lock first choice and ignore feedback",
            "Swap randomly until it fits",
            "Defer constraints to the end",
        ]
        tasks.append(mc_question(f"MF-{i}", 4, question, options, 0))
    return tasks


# ---------- System Creation ----------

def generate_sc_tasks():
    tasks = []
    simple_orders = [
        ["Input", "Processor", "Output"],
        ["Sense", "Transform", "Report"],
        ["Collect", "Validate", "Store"],
        ["Capture", "Process", "Deliver"],
        ["Observe", "Filter", "Notify"],
        ["Listen", "Parse", "Respond"],
        ["Request", "Handle", "Return"],
        ["Intake", "Check", "Emit"],
        ["Record", "Compute", "Display"],
        ["Receive", "Route", "Confirm"],
    ]
    for idx, parts in enumerate(simple_orders, 1):
        options = [
            f"{parts[1]} → {parts[0]} → {parts[2]}",
            " → ".join(parts),
            f"{parts[2]} → {parts[0]} → {parts[1]}",
            f"{parts[1]} → {parts[2]} → {parts[0]}",
        ]
        tasks.append(mc_question(f"SC-{idx}", 1, f"Arrange components {parts} into a valid pipeline.", options, 1))

    for i in range(11, 31):
        branch = i - 10
        question = f"Core C feeds A and B. A must precede D, B precedes E. Scenario {branch}: which completion order respects dependencies?"
        options = [
            "C, A, B, D, E",
            "C, B, A, E, D",
            "A, C, B, D, E",
            "C, A, D, B, E",
        ]
        tasks.append(mc_question(f"SC-{i}", 2, question, options, 0))

    for i in range(31, 41):
        node = i - 30
        question = f"Activation tree {node}: H depends on F and G; F on D and E; D on B and C; B on A. How many nodes must be ready before H?"
        tasks.append(num_question(f"SC-{i}", 3, question, 8))

    for i in range(41, 51):
        layer = i - 40
        question = f"Dynamic constraint {layer}: if X fails, backup XB needs Y and Z refreshed; Y refresh pauses Z. Choose the correct order."
        options = [
            "Pause Z, refresh Y, refresh Z, activate XB",
            "Refresh Y, activate XB, refresh Z",
            "Activate XB, refresh Y, refresh Z",
            "Refresh Z, refresh Y, activate XB",
        ]
        tasks.append(mc_question(f"SC-{i}", 4, question, options, 0))
    return tasks


# ---------- Parallel Hypothesis Management ----------

def generate_ph_tasks():
    tasks = []
    for i in range(1, 11):
        question = f"Scenario {i}: Evidence supports H1 and contradicts H2. Which remains plausible?"
        options = ["Only H1", "Only H2", "Both", "Neither"]
        tasks.append(mc_question(f"PH-{i}", 1, question, options, 0))

    for i in range(11, 31):
        phase = i - 10
        question = f"Phase {phase}: Hypotheses A (early spike), B (late spike), C (constant). Evidence shows early spike then flat. Least plausible?"
        options = ["A", "B", "C", "None"]
        tasks.append(mc_question(f"PH-{i}", 2, question, options, 1))

    for i in range(31, 41):
        scenario = i - 30
        question = f"Scenario {scenario}: H1 needs symmetry, H2 long delay, H3 short delay, H4 immediate. Evidence removes symmetry, favors delay, then caps delay at 2. Which survives?"
        options = ["H1", "H2", "H3", "H4"]
        tasks.append(mc_question(f"PH-{i}", 3, question, options, 3))

    for i in range(41, 51):
        stage = i - 40
        question = f"Stage {stage}: Evidence A removes models using module M. Evidence B requires reversible steps. Evidence C penalizes irreversible steps unless buffered. P uses M irreversibly, Q no M reversible, R no M irreversible unbuffered, S uses buffer reversible. Which remains?"
        options = ["P", "Q", "R", "S"]
        tasks.append(mc_question(f"PH-{i}", 4, question, options, 1))
    return tasks


# ---------- Strategic Structural Cognition ----------

def generate_ssc_tasks():
    tasks = []
    for i in range(1, 11):
        question = f"Chain A→B→C scenario {i}: what happens if B slows?"
        options = [
            "C receives less input",
            "A speeds up automatically",
            "C speeds up",
            "System unaffected",
        ]
        tasks.append(mc_question(f"SSC-{i}", 1, question, options, 0))

    for i in range(11, 31):
        question = f"Iteration {i-10}: Prototype → Limited rollout → Monitor → Scale. Monitoring shows instability. Best next move?"
        options = [
            "Ignore and scale",
            "Return to prototype for fixes",
            "Skip to scale",
            "Cancel project",
        ]
        tasks.append(mc_question(f"SSC-{i}", 2, question, options, 1))

    for i in range(31, 41):
        question = f"Cascading chain W→X→Y→Z with feedback Z→X. If Y throttles, long-term behavior?"
        options = [
            "Lower flow stabilizes after feedback reduces X output",
            "Z accelerates and fixes Y",
            "Chain breaks permanently",
            "Feedback ignored",
        ]
        tasks.append(mc_question(f"SSC-{i}", 3, question, options, 0))

    for i in range(41, 51):
        question = f"Architecture choice {i-40}: Plan Alpha uses redundancy then convergence; Plan Beta single path with checkpoints. Under volatility needing resilience, which is better and why?"
        options = [
            "Plan Alpha; redundancy absorbs volatility",
            "Plan Beta; single path is simpler",
            "Neither; volatility prefers no structure",
            "Plan Beta; checkpoints alone suffice",
        ]
        tasks.append(mc_question(f"SSC-{i}", 4, question, options, 0))
    return tasks


def main():
    write_file("tasks_fl.json", generate_fl_tasks())
    write_file("tasks_rr.json", generate_rr_tasks())
    write_file("tasks_mf.json", generate_mf_tasks())
    write_file("tasks_sc.json", generate_sc_tasks())
    write_file("tasks_ph.json", generate_ph_tasks())
    write_file("tasks_ssc.json", generate_ssc_tasks())


if __name__ == "__main__":
    main()
