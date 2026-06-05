---
layout: default
title: "Flowchart Component Demo"
lang: en
permalink: /flowchart-demo/
---

# Flowchart Component Library

This page demonstrates the HTML-based flowchart components available for Argent Public investigations. All examples use pure HTML/CSS with no JavaScript.

---

## Example 1: Simple Decision Tree

**Use case:** Show a yes/no decision and its consequences

<div class="flowchart">
  <h3 class="flowchart-title">Was there competitive bidding?</h3>
  
  <div class="flow-node start">
    <strong>Government Contract</strong>
    <span class="note">$458M initial budget</span>
  </div>
  
  <div class="flow-arrow">↓</div>
  
  <div class="flow-decision">
    Competitive Bidding Process?
  </div>
  
  <div class="flow-branches">
    <div class="flow-branch">
      <div class="flow-branch-label yes">YES</div>
      <div class="flow-node proper">
        Multiple suppliers compete
      </div>
      <div class="flow-arrow">↓</div>
      <div class="flow-node proper">
        Market forces control costs
      </div>
    </div>
    
    <div class="flow-branch">
      <div class="flow-branch-label no">NO</div>
      <div class="flow-node irregular">
        Single supplier (SAP)
      </div>
      <div class="flow-arrow">↓</div>
      <div class="flow-node irregular">
        No competition on pricing
      </div>
    </div>
  </div>
  
  <div class="flow-convergence">
    <div class="flow-outcome negative">
      <strong>Actual Result:</strong><br>
      $1.1 billion final cost (+140%)
    </div>
  </div>
</div>

---

## Example 2: Timeline (Vertical Linear Flow)

**Use case:** Show chronological events with causation

<div class="flowchart timeline">
  <div class="flow-node start">
    <strong>2017</strong><br>
    Contract signed with SAP
  </div>
  
  <div class="flow-arrow">↓</div>
  
  <div class="flow-node warning">
    <strong>2018-2020</strong><br>
    Costs begin escalating
    <span class="note">No public reporting</span>
  </div>
  
  <div class="flow-arrow">↓</div>
  
  <div class="flow-node warning">
    <strong>2021</strong><br>
    Internal auditors raise concerns
    <span class="note">Warnings not acted upon</span>
  </div>
  
  <div class="flow-arrow">↓</div>
  
  <div class="flow-node irregular">
    <strong>2023</strong><br>
    Project delivered at $1.1B
    <span class="note">+140% over budget</span>
  </div>
  
  <div class="flow-arrow">↓</div>
  
  <div class="flow-node end">
    <strong>2026</strong><br>
    Auditor General Report
    <span class="note">586 pages, 75 hearing days</span>
  </div>
</div>

---

## Example 3: Multi-Branch Process Flow

**Use case:** Show complex decision trees with multiple paths

<div class="flowchart">
  <h3 class="flowchart-title">Public Procurement Decision Tree</h3>
  
  <div class="flow-node start">
    Ministry needs IT system
  </div>
  
  <div class="flow-arrow">↓</div>
  
  <div class="flow-decision">
    Sole-source exemption claimed?
  </div>
  
  <div class="flow-branches">
    <div class="flow-branch">
      <div class="flow-branch-label no">NO</div>
      <div class="flow-node proper">
        Public tender published
      </div>
      <div class="flow-arrow">↓</div>
      <div class="flow-decision">
        3+ bids received?
      </div>
      <div class="flow-arrow">↓</div>
      <div class="flow-node proper">
        Evaluation committee reviews
      </div>
      <div class="flow-arrow">↓</div>
      <div class="flow-outcome">
        Best value selected
      </div>
    </div>
    
    <div class="flow-branch">
      <div class="flow-branch-label yes">YES</div>
      <div class="flow-node warning">
        Justification documented?
      </div>
      <div class="flow-arrow">↓</div>
      <div class="flow-decision">
        Valid reason?
      </div>
      <div class="flow-branches">
        <div class="flow-branch">
          <div class="flow-arrow-label">Yes</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node proper">
            Legal exemption
          </div>
        </div>
        <div class="flow-branch">
          <div class="flow-arrow-label">No</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node irregular">
            Irregular procurement
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

---

## Example 4: Comparison (What Should Have Happened vs. What Happened)

**Use case:** Show regulatory requirements vs. actual events

<div class="flowchart">
  <h3 class="flowchart-title">SAAQclic Procurement: Expected vs. Actual</h3>
  
  <div class="flow-node start">
    Ministry of Health needs IT system (2017)
  </div>
  
  <div class="flow-arrow">↓</div>
  
  <div class="flow-branches">
    <div class="flow-branch">
      <div class="flow-branch-label yes">REGULATORY PATH</div>
      
      <div class="flow-node theoretical">
        Public call for tenders
      </div>
      <div class="flow-arrow faded">↓</div>
      
      <div class="flow-node theoretical">
        Multiple suppliers bid
      </div>
      <div class="flow-arrow faded">↓</div>
      
      <div class="flow-node theoretical">
        Evaluation committee scores bids
      </div>
      <div class="flow-arrow faded">↓</div>
      
      <div class="flow-node theoretical">
        Best value contract awarded
      </div>
      <div class="flow-arrow faded">↓</div>
      
      <div class="flow-outcome">
        Competitive pricing
      </div>
    </div>
    
    <div class="flow-branch">
      <div class="flow-branch-label no">ACTUAL PATH</div>
      
      <div class="flow-node irregular">
        Direct negotiation with SAP
      </div>
      <div class="flow-arrow">↓</div>
      
      <div class="flow-node irregular">
        No competitive bids
      </div>
      <div class="flow-arrow">↓</div>
      
      <div class="flow-node irregular">
        Single-source justification
        <span class="note">"System integration critical"</span>
      </div>
      <div class="flow-arrow">↓</div>
      
      <div class="flow-node irregular">
        SAP contract signed ($458M)
      </div>
      <div class="flow-arrow">↓</div>
      
      <div class="flow-outcome negative">
        Final cost: $1.1 billion (+140%)
      </div>
    </div>
  </div>
</div>

---

## Example 5: Simple Two-Step Process

**Use case:** Show a straightforward cause-and-effect

<div class="flowchart">
  <div class="flow-node start">
    Sole-source contract awarded
  </div>
  
  <div class="flow-arrow thick">↓</div>
  
  <div class="flow-node irregular">
    No competitive pressure on costs
  </div>
  
  <div class="flow-arrow thick">↓</div>
  
  <div class="flow-outcome negative">
    <strong>Cost Overrun</strong><br>
    $458M → $1.1B
  </div>
</div>

---

## Component Reference

### Available CSS Classes

**Containers:**
- `.flowchart` — Main container (centered, with background)
- `.flowchart.timeline` — Vertical timeline variant
- `.flowchart-title` — Optional title/heading

**Nodes (boxes):**
- `.flow-node` — Standard node
- `.flow-node.start` — Starting point (green border)
- `.flow-node.end` — Ending point (green background)
- `.flow-node.proper` — Correct/legal process (green tint)
- `.flow-node.irregular` — Problematic action (red tint)
- `.flow-node.warning` — Cautionary step (yellow tint)
- `.flow-node.theoretical` — Didn't happen (faded gray)

**Decisions:**
- `.flow-decision` — Diamond-shaped decision point (yellow)

**Layout:**
- `.flow-branches` — Container for side-by-side branches
- `.flow-branch` — Individual branch column
- `.flow-branch-label` — Label above branch (add `.yes` or `.no`)
- `.flow-convergence` — Convergence point after branches

**Connectors:**
- `.flow-arrow` — Arrow symbol (use `↓` `→` `←` `↑`)
- `.flow-arrow.thick` — Emphasized arrow (green)
- `.flow-arrow.faded` — De-emphasized arrow (gray)
- `.flow-arrow-label` — Small text label on arrow

**Outcomes:**
- `.flow-outcome` — Final result box (green)
- `.flow-outcome.negative` — Negative result (red)

---

## HTML Structure Template

```html
<div class="flowchart">
  <h3 class="flowchart-title">Optional Title</h3>
  
  <!-- Simple linear flow -->
  <div class="flow-node start">Starting point</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-node">Step 2</div>
  <div class="flow-arrow">↓</div>
  
  <!-- Decision point -->
  <div class="flow-decision">Question?</div>
  
  <!-- Branching -->
  <div class="flow-branches">
    <div class="flow-branch">
      <div class="flow-branch-label yes">YES</div>
      <div class="flow-node proper">Good outcome</div>
    </div>
    <div class="flow-branch">
      <div class="flow-branch-label no">NO</div>
      <div class="flow-node irregular">Bad outcome</div>
    </div>
  </div>
  
  <!-- Convergence -->
  <div class="flow-convergence">
    <div class="flow-outcome">Final result</div>
  </div>
</div>
```

---

## Mobile Behavior

- **Desktop:** Side-by-side branches, full spacing
- **Mobile:** Branches stack vertically, nodes resize
- All flowcharts are fully responsive and print-friendly

---

## Copy-Paste Ready: Minimal Example

```html
<div class="flowchart">
  <div class="flow-node start">Start here</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-node">What happened</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-outcome negative">Bad result</div>
</div>
```
