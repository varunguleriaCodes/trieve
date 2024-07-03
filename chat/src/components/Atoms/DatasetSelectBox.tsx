import { FaSolidCheck } from "solid-icons/fa";
import {
  Show,
  For,
  useContext,
  createSignal,
  createEffect,
  Switch,
  Match,
} from "solid-js";
import {
  Menu,
  MenuItem,
  Popover,
  PopoverButton,
  PopoverPanel,
} from "terracotta";
import { UserContext } from "../contexts/UserContext";
import { DatasetAndUsageDTO } from "../../utils/apiTypes";
import createFuzzySearch from "@nozbe/microfuzz";
import { FiChevronDown, FiChevronUp } from "solid-icons/fi";

export const DatasetSelectBox = () => {
  const userContext = useContext(UserContext);
  const $datasetsAndUsages = userContext.datasetsAndUsages;
  const $currentDataset = userContext.currentDataset;

  const [datasetSearchQuery, setDatasetSearchQuery] = createSignal("");

  const [datasetSearchResults, setDatasetSearchResults] = createSignal<
    DatasetAndUsageDTO[]
  >([]);
  createEffect(() => {
    const datasetListOrEmpty = userContext.datasetsAndUsages?.() ?? [];
    if (datasetSearchQuery() === "") {
      setDatasetSearchResults(datasetListOrEmpty);
    } else {
      const fuzzy = createFuzzySearch(datasetListOrEmpty, {
        getText: (item: DatasetAndUsageDTO) => {
          return [item.dataset.name];
        },
      });
      const results = fuzzy(datasetSearchQuery() ?? "");
      setDatasetSearchResults(results.map((result) => result.item));
    }
  });

  return (
    <Show when={$datasetsAndUsages?.().length != 0}>
      <Popover defaultOpen={false} class="relative">
        {({ isOpen, setState }) => (
          <>
            <PopoverButton
              aria-label="Toggle filters"
              type="button"
              class="flex min-w-fit items-center space-x-1 pb-1 text-sm"
            >
              <span class="line-clamp-1 min-w-fit text-left text-sm">
                {$currentDataset?.()?.dataset.name}
              </span>
              <Switch>
                <Match when={isOpen()}>
                  <FiChevronUp class="h-3.5 w-3.5" />
                </Match>
                <Match when={!isOpen()}>
                  <FiChevronDown class="h-3.5 w-3.5" />
                </Match>
              </Switch>
            </PopoverButton>
            <Show when={isOpen()}>
              <PopoverPanel
                unmount={false}
                class="absolute bottom-5 left-0 z-10 mt-2 h-fit w-[180px] rounded-md border bg-white p-1 dark:bg-neutral-800"
              >
                <Menu class="mx-1 space-y-0.5">
                  <input
                    placeholder="Search datasets..."
                    class="mb-2 flex w-full items-center justify-between rounded bg-neutral-300 p-1 text-sm text-black outline-none dark:bg-neutral-700 dark:hover:text-white dark:focus:text-white"
                    onInput={(e) => {
                      setDatasetSearchQuery(e.target.value);
                    }}
                    value={datasetSearchQuery()}
                  />

                  <For each={datasetSearchResults()}>
                    {(datasetItem) => {
                      return (
                        <MenuItem
                          as="button"
                          classList={{
                            "flex w-full items-center justify-between rounded p-1 focus:text-black focus:outline-none dark:hover:text-white dark:focus:text-white hover:bg-neutral-300 hover:dark:bg-neutral-700":
                              true,
                            "bg-neutral-300 dark:bg-neutral-700":
                              datasetItem.dataset.id ===
                              $currentDataset?.()?.dataset.id,
                          }}
                          onClick={(e: Event) => {
                            e.preventDefault();
                            e.stopPropagation();
                            userContext.setCurrentDataset(datasetItem);
                            setState(false);
                          }}
                        >
                          <div class="break-all px-1 text-left text-sm">
                            {datasetItem.dataset.name}
                          </div>
                          <Show
                            when={
                              datasetItem.dataset.id ==
                              $currentDataset?.()?.dataset.id
                            }
                          >
                            <span>
                              <FaSolidCheck class="text-sm" />
                            </span>
                          </Show>
                        </MenuItem>
                      );
                    }}
                  </For>
                </Menu>
              </PopoverPanel>
            </Show>
          </>
        )}
      </Popover>
    </Show>
  );
};
