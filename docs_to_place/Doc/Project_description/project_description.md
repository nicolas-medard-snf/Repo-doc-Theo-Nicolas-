# Project Description

## The clinical problem

Patients with triple-negative (TNBC) and HER2-positive breast cancer are often treated *before* surgery, with neoadjuvant chemotherapy or targeted agents, in the hope of shrinking the tumor and improving long-term outcomes. The strongest signal that this strategy worked is a **pathological complete response (pCR)**: no residual invasive cancer found at surgery. The trouble is that pCR is far from guaranteed. Some patients clear their disease entirely while others, treated with the same regimen, see little benefit and absorb the toxicity of treatment for nothing. Today there is no reliable way to know in advance which patient will fall into which group.

This project is an attempt to close that gap from the DNA side. Its working hypothesis is that the answer is partly written in the tumor's genome, and that **Whole Exome Sequencing (WES)** can expose the mutational drivers and biomarkers that separate responders from non-responders.

## What the project actually builds

Rather than running a single statistical model, the project assembles the *evidence base* that any such model would need: a curated, structured body of knowledge about which genomic features predict neoadjuvant response in these two breast cancer subtypes. Concretely, it ingests the scientific literature and sequencing-method know-how, tags each piece of evidence along a fixed set of dimensions, and from that distills a defensible, ranked shortlist of candidate genes.

The end product is therefore not a clinical recommendation but a **decision-support substrate**: a vetted candidate-gene list, with the reasoning and provenance attached, that a downstream AI can apply to real WES datasets. The deliberate emphasis is on separating genes that genuinely drive response from the much larger pool of genomic noise, so that downstream analysis spends its effort where the signal actually is.

## How the knowledge is organized

Because a gene rarely "predicts response" in the abstract, the project refuses to store evidence as a flat pile of papers. Each finding is understood through five complementary lenses, each maintained as its own corpus:

- **Genomic signal** — what *kind* of biological feature a gene represents (DNA-repair/HRD, tumor mutational burden, immune activity, drivers and copy-number changes, epigenetic regulation).
- **Therapeutic context** — which *drug* the signal is actually predictive for, since an HRD signature speaks to platinum/PARP inhibitors while an immune signal speaks to checkpoint therapy.
- **Cancer subtype** — whether the claim holds for TNBC, HER2+, or neither, preventing a biomarker validated in one subtype from being misapplied to another.
- **Clinical endpoint** — whether the evidence is tied directly to pCR, or only to softer outcomes like survival or resistance.
- **Study type** — what kind of evidence it is (method, model, trial, cohort, sequencing platform), which sets how much weight it should carry.

These lenses are not independent. Sequencing methods determine how a signal can even be computed; a raw signal only becomes meaningful once paired with a drug and a subtype; and everything is ultimately judged against whether it predicts pCR. Crucially, validated pCR results feed back to re-rank the candidate genes, so the shortlist tightens as more evidence accumulates rather than growing stale.

## What it deliberately leaves out

The project stays narrow on purpose. It is about *breast* cancer, *pCR*, and *DNA-derivable, treatment-predictive* signals. It is not a survey of cancer biology in general, not a study of survival or recurrence as primary goals, and not a home for proteomics, imaging, or germline-risk genetics except where they directly inform a treatment-predictive genomic signal. It does not invent data, does not alter source files during ingestion, and does not issue treatment advice. These boundaries exist so the candidate-gene shortlist stays sharp and the system does not drift into adjacent but unhelpful territory.

## Where it starts

The genomic-signal lens is grown first, because it is the only one that produces actual genes — the substrate everything else exists to filter and contextualize. Until that list exists, the therapeutic, subtype, and endpoint lenses have nothing to act on. Within it, DNA-repair/HRD and immune-microenvironment biology take priority, since those carry the most established, treatment-linked pCR biomarkers in breast cancer and therefore give the downstream analysis usable candidates the soonest.